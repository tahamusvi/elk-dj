from .base_gateway import PaymentGateway,response_for_front
import json
import requests
from config.settings import MERCHANT
from ..models import Payment,PaymentAllocation
from config.field_choices import PaymentStatusChoices



class ZarinpalGateway(PaymentGateway):

    def request_url(self):
        base_url = 'sandbox' if self.sandbox else 'www'
        return f"https://{base_url}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"

    def verify_url(self):
        base_url = 'sandbox' if self.sandbox else 'www'
        return f"https://{base_url}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"

    def startpay_url(self):
        base_url = 'sandbox' if self.sandbox else 'www'
        return f"https://{base_url}.zarinpal.com/pg/StartPay/"
  
    def create_redirect_url(self,amount,payment):

        data = {
            "MerchantID": MERCHANT,
            "Amount": amount,
            "Description": self.description,
            # "Phone": user.phoneNumber,
            "Phone": "09303016386",
            "CallbackURL": self.callback_url,
        }
        data = json.dumps(data)

        # set content length by data
        headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
        try:
            response = requests.post(self.request_url(), data=data,headers=headers, timeout=10)
            print("-----------------")
            print(response)
            response_dict = json.loads(response.text)
            status = response_dict['Status']
            authority = response_dict['Authority']

            print(response_dict)


            if(status == 100):
                redirect_url = f"{self.startpay_url()}{authority}"

                payment.authority = authority
                payment.save()

                return {'redirect_url':redirect_url,}
                
            
            return {'message':response_for_front['not_connected'],}

        
        except requests.exceptions.Timeout:
            return {'message':response_for_front['too_long'],}
        except requests.exceptions.ConnectionError:
            return {'message':response_for_front['not_success_connect'],}


    def verify_payment(self,amount,front_status,payment):

        if(front_status == "NOK"):
            return {'message':response_for_front['not_success_connect'],}
        
        elif(front_status == "OK"):
            data = {
                "MerchantID": MERCHANT,
                "Amount": amount,
                "Authority": payment.authority,
            }
        
            data = json.dumps(data)
            # set content length by data
            headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
            response = requests.post(self.verify_payment(), data=data,headers=headers)

            response_dict = json.loads(response.text)
            status_gateway = response_dict['Status']
            RefID = response_dict['RefID']

            if status_gateway == 100 or status_gateway == 101:
                    
                    payment.ref_id = RefID
                    payment.status = PaymentStatusChoices.IN_PROGRESS
                    payment.save()

                    payment_allocations = PaymentAllocation.objects.filter(payment=payment)
                    for allocation in payment_allocations:
                        wallet = allocation.wallet
                        amount_to_pay = allocation.amount
                        
                        wallet.pay_debt(amount_to_pay)
                                
                    return {'message':response_for_front['success'],}

            else:
                return {'message':response_for_front['not_success_connect'],}
        else:
            return {'message':response_for_front['not_success_connect'],}

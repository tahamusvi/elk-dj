response_for_front = {
    "not_connected" : ' اتصال به درگاه ناموفق بود.',
    "too_long" : 'زمان بیش حد سپری شده برای اتصال به درگاه.',
    "not_success_connect" : 'اتصال ناموفق.',
    "success" : 'پرداخت با موفقیت انجام شد.',
    "payed" : 'پرداخت انجام شده بوده است.',
    "not_upload" : 'آپلود با مشکل مواجه شد.',
    "success_upload" : "آپلود با موفقیت انجام شد. برای پیگیری سفارش به داشبورد مراجعه کنید.",
    "user_not_match" : "این کاربر دسترسی لازم ندارد"
}


class PaymentGateway():
    name = "name for gateway"
    description = "description about gateway"
    callback_url = "url call back for gateway return user"
    sandbox = True
    is_active = False

    
    def request_url(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    def verify_url(self):
        raise NotImplementedError("This method should be implemented by subclasses")    
    
    def create_redirect_url(self):
        raise NotImplementedError("This method should be implemented by subclasses")
    
    def verify_payment(self):
        raise NotImplementedError("This method should be implemented by subclasses")



from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import *
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import *
from ..serializers import *

messages_for_front = {
    "login_required": "ابتدا لاگین کنید.",
    "403_error": "اجازه دسترسی وجود ندارد.",
    'wallet_not_found': "ولتی یافت نشد.",
}

class UserPaymentAPIView(APIView):
    serializer_class = PaymentSerializer

    def get(self, request):
        try:
            payments = Payment.objects.all()
            serializer = PaymentSerializer(payments, many=True)
            return Response(serializer.data)

        except Wallet.DoesNotExist:
            return Response(
                {"message": messages_for_front['wallet_not_found']},
                status=status.HTTP_404_NOT_FOUND,
            )



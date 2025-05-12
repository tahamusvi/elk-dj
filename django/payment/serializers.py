from rest_framework import serializers
from .models import *
# from drf_spectacular.utils import extend_schema_field

class PaymentStatus(models.TextChoices):
        SUCCESS = 'تراکنش موفق'
        FAILURE = 'تراکنش ناموفق'
        AMOUNTCONFLICT = 'مغایرت مبلغ'
        RESNUMUSED = 'شناسه خرید تکراری'
        RESNUMNOTFOUND = 'شناسه خرید یافت نشد'
        NODATA = 'نامشخص'
        INTERNALERRORR = 'خطای داخلی درگاه'
        VERIFYDATACONFLICT = 'مغایرت پارامتر های بانکی'
        NOT_FOUND = 'پرداخت یافت نشد.'

class PaymentResponseSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=PaymentStatus.choices)

class PaymentSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = [
            "id",
            "ref_id",
            "authority",
            "amount",
            "created_at",
            "shamsi_date",
            "status_display",
        ]



class WalletAllocationSerializer(serializers.Serializer):
    wallet_id = serializers.IntegerField()
    amount = serializers.IntegerField()


class UserBalanceSerializer(serializers.Serializer):
    total_balance = serializers.IntegerField()


class VerifyPaymentResponseSerializer(serializers.Serializer):
    errCode = serializers.IntegerField()
    result = serializers.JSONField()
    status_gateway = serializers.IntegerField()
    transactionId = serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
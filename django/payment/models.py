from django.db import models
from django.utils import timezone
from config.field_choices import PaymentStatusChoices



class Wallet(models.Model):
    balance = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    financial_cap = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.id}: {self.balance}ریال"

    @property
    def shamsi_created(self):
        return self.created_at

    @property
    def shamsi_updated(self):
        return self.updated_at
    
    @property
    def action_count(self):
        return abs((self.financial_cap - self.balance) // 100)
    
    def decrease_pay(self):
        self.balance -= 100
        self.save()


    def pay_debt(self,amount):
        self.balance += amount
        self.save() 

    def get_debt(self):
        if self.balance < 0:
            return self.balance
        else:
            return 0


class Payment(models.Model):
    ref_id = models.CharField(max_length=100, null=True, blank=True)
    authority = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    amount = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=PaymentStatusChoices.choices,
        default=PaymentStatusChoices.PENDING,
    )

    def __str__(self):
        return f"{self.id} - {self.amount}"

    @property
    def shamsi_date(self) -> str:
        return self.created_at

    def days_since_creation(self) -> str:
        now = timezone.now()
        created_naive = timezone.make_naive(
            self.created_at, timezone.get_default_timezone()
        )
        created_aware = timezone.make_aware(
            created_naive, timezone.get_default_timezone()
        )
        days = (now - created_aware).days
        return f"{days} روز پیش"


class PaymentAllocation(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name="allocations")
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return f"Payment {self.payment.id} - Wallet {self.wallet.id}: {self.amount}"
from django.db import models 

class PaymentStatusChoices(models.TextChoices):
    FAIL = 'fail', 'عدم موفقیت'
    IN_PROGRESS = 'successful', 'انجام شده'
    PENDING = 'pending', 'نامشخص'
    DISCREPANCY = 'discrepancy', 'مغایرت'


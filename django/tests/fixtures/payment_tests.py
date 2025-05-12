import pytest
from payment.models import Payment

@pytest.mark.django_db
def test_payment_count():
    assert Payment.objects.count() == 8

@pytest.mark.django_db
def test_pending_payments():
    pending_payments = Payment.objects.filter(status='pending')
    assert pending_payments.count() == 3

@pytest.mark.django_db
def test_successful_payments():
    successful_payments = Payment.objects.filter(status='successful')
    assert successful_payments.count() == 3

@pytest.mark.django_db
def test_failed_payments():
    failed_payments = Payment.objects.filter(status='fail')
    assert failed_payments.count() == 2

@pytest.mark.django_db
def test_payment_ref_id():
    successful_payments = Payment.objects.filter(status='successful')
    for payment in successful_payments:
        assert payment.ref_id is not None

@pytest.mark.django_db
def test_payment_amount():
    payment = Payment.objects.get(pk=1)
    assert payment.amount == 15000
    payment = Payment.objects.get(pk=2)
    assert payment.amount == 25000
    payment = Payment.objects.get(pk=3)
    assert payment.amount == 5000

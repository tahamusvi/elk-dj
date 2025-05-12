import pytest
from payment.models import Wallet
from django.contrib.auth import get_user_model

User = get_user_model()
@pytest.mark.django_db
def test_check_debt_user():

    wallet = Wallet.objects.create(balance=-200, financial_cap=5000)

    wallet.decrease_pay()
    wallet.decrease_pay()
    wallet.decrease_pay()


    assert wallet.balance == -500

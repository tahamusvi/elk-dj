import pytest
from payment.serializers import WalletAllocationSerializer

@pytest.mark.django_db
def test_wallet_allocation_serializer_valid():
    valid_data = {
        "wallet_id": 1,
        "amount": 1000,
    }
    
    serializer = WalletAllocationSerializer(data=valid_data)
    
    assert serializer.is_valid()
    assert serializer.validated_data["wallet_id"] == 1
    assert serializer.validated_data["amount"] == 1000

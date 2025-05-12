import pytest
from django.core.management import call_command
from httpx import AsyncClient
from config.asgi import application

@pytest.fixture(scope="session")
def django_db_setup(django_db_blocker):
    with django_db_blocker.unblock():
        call_command("load_all_fixtures", "--noinput")



@pytest.fixture
async def async_client():
    async with AsyncClient(app=application, base_url="http://127.0.0.1:8000/") as client:
        yield client

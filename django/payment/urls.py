from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# ---------------------------
app_name = "payment"

urlpatterns = [
    path("user/", UserPaymentAPIView.as_view()),
]


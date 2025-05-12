from datetime import timedelta
from .base import *

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "config.pagination.CustomPagination",
    "PAGE_SIZE": 5,
}

SPECTACULAR_SETTINGS = {
    "TITLE": "API Documentation",
    'POSTPROCESSING_HOOKS': [],
}

DJOSER = {
    "LOGIN_FIELD": "phone_number",
    "USER_CREATE_PASSWORD_RETYPE": False,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": False,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": False,
    "SEND_CONFIRMATION_EMAIL": False,
    "SET_PASSWORD_RETYPE": False,
    "PASSWORD_RESET_CONFIRM_URL": "resetpassword/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_URL": "resetphone/{uid}/{token}",
    "ACTIVATION_URL": "verification/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": False,
    "SERIALIZERS": {
        "user_create": "core.serializers.UserCreateSerializer",
        "user": "core.serializers.UserCreateSerializer",
        "user_delete": "djoser.serializers.UserDeleteSerializer",
    },
}

ACCESS_TOKEN_LIFETIME = env("ACCESS_TOKEN_LIFETIME", "00-00-01").split("-")
REFRESH_TOKEN_LIFETIME = env("REFRESH_TOKEN_LIFETIME", "00-00-10").split("-")

acces_kwargs = {
    "days": int(ACCESS_TOKEN_LIFETIME[0]),
    "hours": int(ACCESS_TOKEN_LIFETIME[1]),
    "minutes": int(ACCESS_TOKEN_LIFETIME[2]),
}

refresh_kwargs = {
    "days": int(REFRESH_TOKEN_LIFETIME[0]),
    "hours": int(REFRESH_TOKEN_LIFETIME[1]),
    "minutes": int(REFRESH_TOKEN_LIFETIME[2]),
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": (
        "JWT",
    ),
    "ACCESS_TOKEN_LIFETIME": timedelta(**acces_kwargs),
    "REFRESH_TOKEN_LIFETIME": timedelta(**refresh_kwargs),
    "UPDATE_LAST_LOGIN": True,
}

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularJSONAPIView,
)
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar


urlpatterns = [
    path("admin/", admin.site.urls),

    path("auth/", include("core.urls")),
    path("payment/", include("payment.urls")),
    path("api-schema", SpectacularAPIView.as_view(), name="schema"),
    path("api-schema-json", SpectacularJSONAPIView.as_view(), name="schema"),
    path("", SpectacularSwaggerView.as_view(url_name="schema")),
    path("api-auth/", include("rest_framework.urls")),
    path('__debug__/', include(debug_toolbar.urls)),

]






if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

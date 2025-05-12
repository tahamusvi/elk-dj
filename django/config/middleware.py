from django.http import HttpResponseNotAllowed
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
import re


class CSPMiddleware(MiddlewareMixin):
    async def __call__(self, request):
        if settings.DEBUG:
            print("CSP request path ------->", request.path)

        response = await self.get_response(request)
        swagger_ui_pattern = re.compile(r"^/schema/swagger-ui/")
        safe_list = ["/favicon.ico", "/"]

        if (request.path in safe_list) or swagger_ui_pattern.match(request.path):
            # Apply a more permissive CSP policy for Swagger UI
            response["Content-Security-Policy"] = (
                "default-src 'self'; "
                "script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdn.jsdelivr.net; "
                "style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; "
                "img-src 'self' data: https://cdn.jsdelivr.net; "
                "font-src 'self' data: https://cdn.jsdelivr.net; "
                "connect-src 'self' https://cdn.jsdelivr.net; "
                "frame-src 'self' https://cdn.jsdelivr.net; "
                "frame-ancestors 'self'"  # Added frame-ancestors directive
            )
            response["X-Frame-Options"] = "SAMEORIGIN"
        else:
            # Apply the restrictive CSP policy for other endpoints
            response["Content-Security-Policy"] = (
                "default-src 'self'; "
                "script-src 'self'; "
                "style-src 'self'; "
                "img-src 'self'; "
                "font-src 'self'; "
                "connect-src 'self'; "
                "frame-src 'none'; "  # Update frame-src to 'none'
                "frame-ancestors 'none'"  # Added frame-ancestors directive
            )
            response["X-Frame-Options"] = "DENY"
        return response


class DisableOptionsMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method == "OPTIONS":
            return HttpResponseNotAllowed([])
        return None


class DisableAllowHeaderMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if "Allow" in response:
            del response["Allow"]
        return response

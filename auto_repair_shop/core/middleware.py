from django.core.exceptions import PermissionDenied

from auto_repair_shop.settings import BLOCKED_IP


class FilterIPtMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        blocked_ip = BLOCKED_IP
        ip = request.META.get('REMOTE_ADDR')
        if ip in blocked_ip:
            raise PermissionDenied
        response = self._get_response(request)
        return response


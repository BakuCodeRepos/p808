from threading import current_thread
from django.utils.deprecation import MiddlewareMixin

_requests = {}

def get_current_request():
    t = current_thread()
    return None if t not in _requests else _requests[t]


class RequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        _requests[current_thread()] = request

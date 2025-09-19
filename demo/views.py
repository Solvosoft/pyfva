from functools import wraps
import json
from django.http import JsonResponse
from django.core.cache import cache

def check_transaction(request, idtransaction):
    data = cache.get(str(idtransaction))
    if data is None:
        return JsonResponse({'ok': False})
    data['ok'] = True
    return JsonResponse(data)


def json_wrapper(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body.decode('utf-8'))
                kwargs['data'] = data
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON'}, status=400)
        return JsonResponse(view_func(request, *args, **kwargs))
    return wrapper
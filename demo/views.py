from django.http import JsonResponse
from django.core.cache import cache

def check_transaction(request, idtransaction):
    data = cache.get(str(idtransaction))
    if data is None:
        return JsonResponse({'ok': False})
    data['ok'] = True
    return JsonResponse(data)
from django.views.decorators.csrf import csrf_exempt

from pyfva import load_module_responder
from pyfva.conf import settings
from pyfva import logger

receptorclient = load_module_responder(settings.RECEPTOR_CLIENT)

def valide_servicio():
    logger.info({'message': "Valide servicio accionado", 'data': 'valide_servicio', 'location': __file__})
    return True

def reciba_notificacion(data):
    logger.info({'message': "Notificación recibida", 'data': data, 'location': __file__})


def valide_servicio_view(request):
    dev = receptorclient.valide_servicio()
    return {"content":dev}

@csrf_exempt
def recibe_notificacion(request, *args, **kwargs):
    result = kwargs['data']

    data = {
        'id_solicitud': result['IdDeLaSolicitud'],
        'documento': result['DocumentoFirmado'],
        'fue_exitosa': result['FueExitosa'],
        'codigo_error': result['CodigoDeError'],
        'hash_docfirmado': result['HashDocumentoFirmado'],
        'hash_id': result['IDAlgoritmoHashDocumentoFirmado'],
        'hash_bytes': result['HashDelDocumentoFirmadoEnBytes']
    }
    dev = receptorclient.reciba_notificacion(data)
    return {"content":True}

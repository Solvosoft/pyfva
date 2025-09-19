import base64

from django.core.cache import cache
from pyfva import logger

def get_document(document):
    """
    Comprueba si el documento se puede leer o no, si el archivo es correcto lo retorna, si no retorna None
    :param document:
    :return:
    """
    if type(document) == str:
        return document
    return None

def reciba_notificacion(data):
    """
    Recibe la notificación del BCCR

    :params data: Es un diccionario con los siguientes atributos

        * **id_solicitud:**  Id de la solicitud del BCCR
        * **documento:** Documento firmado
        * **fue_exitosa:** si fue exitosa la firma
        * **codigo_error:** código de error
        * **hash_docfirmado:** Hash del documento ya firmado
        * **hash_id:**  id del hash con que se genero el hash_docfirmado puede ser 1. Sha256, 2. Sha384  3. Sha512

    No requiere retornar nada

    """
    logger.debug({'message': "Recibe notificacion", 'data': {"exitosa": data.get('fue_exitosa', False),
                                                             "id": data['id_solicitud']}, 'location': __file__})
    if 'documento' in data:
        data['documento'] = get_document(data['documento'])
    if data.get('fue_exitosa', False):
        try:
           documento = base64.b64decode(data['documento']).decode()
        except:
           documento = ''
        if '01-0129-0129' in documento:
            data['codigo_error'] = 12
    cache.set(data['id_solicitud'], data)
    if data['codigo_error'] == 12:
        raise


def valide_servicio():
    """
    Valida el si el servicio está disponible

    :returns:
        True si el servicio está disponible,
        False si no lo está
    """
    logger.debug({'message': "Recibe valide el servicio", 'data': { }, 'location': __file__})

    return True

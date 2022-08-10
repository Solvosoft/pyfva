from django.core.cache import cache

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

    cache.set(data['id_solicitud'], data)



def valide_servicio():
    """
    Valida el si el servicio está disponible

    :returns:
        True si el servicio está disponible,
        False si no lo está
    """

    return True
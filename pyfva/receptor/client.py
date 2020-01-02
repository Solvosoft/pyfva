'''
Administra las respuestas recibidas del BCCR, para ponerlo en funcionamiento se debe crear una aplicación web,
por ejemplo en django y agrear lo siguiente en urls.py

.. code:: python

    from pyfva.receptor.ws_service import ResultadoDeSolicitudSoap_SERVICE
    from soapfish.django_ import django_dispatcher
    dispatcher = django_dispatcher(ResultadoDeSolicitudSoap_SERVICE)

    urlpatterns = [
         ...
    url(r'^wcfv2\/Bccr\.Sinpe\.Fva\.EntidadDePruebas\.Notificador\/ResultadoDeSolicitud\.asmx$', 
    dispatcher, name="receptor_fva"),
    ]
    
'''

from pyfva import logger


def reciba_notificacion(data):
    """
    Recibe la notificación del BCCR

    :params data: Es un diccionario con los siguientes atributos

        * **id_solicitud:**  Id de la solicitud del BCCR
        * **documento:** Documento firmado
        * **fue_exitosa:** si fue exitosa la firma
        * **codigo_error:** código de error

    No requiere retornar nada

    """
    logger.debug({'message':"Receptor: reciba notificación", 'data':
                 data, 'location': __file__})


def valide_servicio():
    """
    Valida el si el servicio está disponible

    :returns:
        True si el servicio está disponible, 
        False si no lo está
    """

    dev = True
    logger.debug({'message':"Receptor: reciba notificación", 'data': dev, 'location': __file__})
    return dev

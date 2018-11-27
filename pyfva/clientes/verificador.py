'''
Created on 20 jul. 2017

@author: luis
'''
from pyfva.soap.verificador import ValideElServicio, VerificadorSoapServiceStub,\
    ExisteUnaSolicitudDeFirmaCompleta

from pyfva.soap import settings

import logging
from pyfva.constants import get_text_representation, ERRORES_VERIFICACION
logger = logging.getLogger('pyfva')


class ClienteVerificador(object):
    """Verifica si una firma ha sido completada

    .. note:: 
        Los parámetros negocio y entidad de momento no son requeridos, pero puede que en un futuro cercano
        lo sean, por lo que se recomienda suministrarlos.

    :param negocio: número de identificación del negocio (provisto por el BCCR)
    :param entidad: número de identificación de la entidad (provisto por el BCCR)
    """

    DEFAULT_ERROR = {
        'codigo_error': 1,
        'texto_codigo_error': get_text_representation(ERRORES_VERIFICACION, 1),
        'existe_firma': False,
        'fue_exitosa': False

    }

    def __init__(self,
                 negocio=settings.DEFAULT_BUSSINESS,
                 entidad=settings.DEFAULT_ENTITY):
        self.negocio = negocio
        self.entidad = entidad

    def existe_solicitud_de_firma_completa(self, identificacion):
        """Verifica si una solicitud de firma ha sida completada por el usuario en el sistema del BCCR

        :param identificacion: número de identificación de la persona

        Retorna una diccionario con los siguientes elementos, en caso de error retorna
        **DEFAULT_ERROR**.

        :returns:   
            **codigo_error:** Número con el código de error 0 es éxito

            **texto_codigo_error:** Descripción del error

            **exitosa:** True si fue exitosa, False si no lo fue

            **existe_firma:** Retorna True si hay un proceso de firma activo o False si no.

        """
        logger.info("Verificador: existe solicitud de firma completa %s" %
                    (identificacion, ))
        try:
            dev = self._existe_solicitud_de_firma_completa(identificacion)
        except Exception as e:
            logger.error(
                "Verificador: existe_solicitud_de_firma_completa %s" % (e, ))
            dev = self.DEFAULT_ERROR

        logger.debug("Verificador: existe solicitud de firma completa %s %r" %
                     (identificacion, dev))
        return dev

    def validar_servicio(self):
        """
        Valida si el servicio está disponible.  

        :returns: True si lo está o False si ocurrió algún error contactando al BCCR o el servicio no está disponible
        """
        dev = self._validar_servicio()
        logger.debug("Verificador: validar servicio %r" %
                     (dev,))
        return dev

    # Private methods
    def _existe_solicitud_de_firma_completa(self, identificacion):
        stub = VerificadorSoapServiceStub()
        options = ExisteUnaSolicitudDeFirmaCompleta()
        options.laCedulaDelUsuario = identificacion
        status = stub.ExisteUnaSolicitudDeFirmaCompleta(options)
        result = status.soap_body.ExisteUnaSolicitudDeFirmaCompletaResult
        return self._extract_solicitud_firma_completa(result)

    def _extract_solicitud_firma_completa(self, result):
        dev = {}
        dev.update(self.DEFAULT_ERROR)
        dev['codigo_error'] = result.CodigoDeError
        dev['texto_codigo_error'] = get_text_representation(
            ERRORES_VERIFICACION, result.CodigoDeError)
        dev['existe_firma'] = result.FueExitosa
        dev['fue_exitosa'] = result.ExisteUnaFirmaCompleta
        return dev

    def _validar_servicio(self):
        stub = VerificadorSoapServiceStub()
        option = ValideElServicio()
        try:
            status = stub.ValideElServicio(option)
            dev = status.soap_body.ValideElServicioResult
        except Exception as e:
            logger.error("Verificador: Servicio de verificación fallando %s" %
                         (e,))

            dev = False
        return dev

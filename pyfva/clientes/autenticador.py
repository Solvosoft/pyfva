# encoding: utf-8

'''
Created on 18 jul. 2017

@author: luis
'''
from pyfva.soap.autenticador import AutenticadorSoapServiceStub,\
    RecibaLaSolicitudDeAutenticacion, SolicitudDeAutenticacion, ValideElServicio

from datetime import datetime
from pyfva.soap import settings
import logging
from pyfva.constants import ERRORES_AL_SOLICITAR_FIRMA, get_text_representation

logger = logging.getLogger('pyfva')


class ClienteAutenticador(object):
    """Permite autenticar una persona utilizando los servicios del BCCR

    .. note:: 
        Recuerde la política del banco es *no nos llame, nosotros lo llamamos*

    :param negocio: número de identificación del negocio (provisto por el BCCR)
    :param entidad: número de identificación de la entidad (provisto por el BCCR)
    """

    DEFAULT_ERROR = {
        'codigo_error': 1,
        'texto_codigo_error': get_text_representation(
            ERRORES_AL_SOLICITAR_FIRMA, 1),
        'codigo_verificacion': 'N/D',
        'tiempo_maximo': 1,
        'id_solicitud': 0
    }

    def __init__(self,
                 negocio=settings.DEFAULT_BUSSINESS,
                 entidad=settings.DEFAULT_ENTITY):
        self.negocio = negocio
        self.entidad = entidad

    def get_now(self):
        return datetime.now()

    def solicitar_autenticacion(self, identificacion, id_funcionalidad=-1):
        """Solicita al BCCR la autenticación de la identificacion, 
        recuerde, la política del BCCR es: *no nos llame, nosotros lo llamamos*,
        por lo que los valores devueltos corresponden al estado de la petición y 
        no al resultado de la firma

        :param identificacion: número de identificación de la persona ver  `Formato identificacion <formatos.html#formato-de-identificacion>`_.
        :param id_funcionalidad: Identificación de la funcionalidad del programa externo, se usa para dar seguimiento a la operación, * No obligatorio

        Retorna una diccionario con los siguientes elementos, en caso de error retorna
        **DEFAULT_ERROR**.


        :returns:   
            **codigo_error:** Número con el código de error 0 es éxito

            **texto_codigo_error:** Descripción del error

            **codigo_verificacion:** str con el código de verificación de la trasacción, se muestra al usuario

            **tiempo_maximo:** Tiempo máximo de duración de la solicitud en segundos

            **id_solicitud:** Número de identificación de la solicitud

        """
        logger.info("Autenticador: Solicitar_autenticacion %s" %
                    (identificacion, ))
        request = SolicitudDeAutenticacion.create(
            self.negocio,
            self.get_now(),
            id_funcionalidad,
            self.entidad,
            identificacion
        )

        logger.debug("Autenticador: Solicitar_autenticacion Fin %r %r %r %r" % (
            self.negocio,
            self.get_now().isoformat(),
            self.entidad,
            identificacion
        ))
        try:
            dev = self._solicitar_autenticacion(request)
        except:
            dev = self.DEFAULT_ERROR

        logger.debug("Autenticador: Solicitar_autenticacion %r" % (dev,))
        return dev

    def validar_servicio(self):
        """
        Valida si el servicio está disponible.  

        :returns: True si lo está o False si ocurrió algún error contactando al BCCR o el servicio no está disponible
        """

        dev = self._validar_servicio()
        logger.debug("Autenticador: validar_servicio %r" %
                     (dev, ))

        return dev

    def extrae_resultado(self, solicitud,  resultado):
        """Convierte la infromación obtenida del servicio SOAP a python

        :param solicitud:  Objeto de solicitud del tipo *pyfva.soap.autenticador.SolicitudDeAutenticacion*
        :param resultado: Objeto de respuesta del tipo *pyfva.soap.autenticador.RecibaLaSolicitudDeAutenticacionResult* 

        Retorna una diccionario con los siguientes elementos, en caso de error retorna
        **DEFAULT_ERROR**.

        :returns:   
            **codigo_error:** Número con el código de error 0 es éxito

            **texto_codigo_error:** Descripción del error

            **codigo_verificacion:** str con el código de verificación de la trasacción

            **tiempo_maximo:** Tiempo máximo de duración de la solicitud en segundos

            **id_solicitud:** Número de identificación de la solicitud

        """

        try:
            data = self._extrae_resultado(solicitud,  resultado)
        except Exception as e:
            logger.error('Autenticador: extrayendo datos %s' % (e, ))
            data = self.DEFAULT_ERROR
        return data

    def _solicitar_autenticacion(self, request):
        stub = AutenticadorSoapServiceStub()
        options = RecibaLaSolicitudDeAutenticacion()
        options.laSolicitud = request

        status = stub.RecibaLaSolicitudDeAutenticacion(options)

        return self.extrae_resultado(
            request, status.soap_body.RecibaLaSolicitudDeAutenticacionResult)

    def _extrae_resultado(self, request, result):
        data = {
            'codigo_error': result.CodigoDeError,
            'texto_codigo_error': get_text_representation(
                ERRORES_AL_SOLICITAR_FIRMA, result.CodigoDeError),
            'codigo_verificacion': result.CodigoDeVerificacion,
            'tiempo_maximo': result.TiempoMaximoDeFirmaEnSegundos,
            'id_solicitud': result.IdDeLaSolicitud,
            'resumen': result.ResumenDelDocumento
        }
        return data

    def _validar_servicio(self):
        stub = AutenticadorSoapServiceStub()
        option = ValideElServicio()
        try:
            status = stub.ValideElServicio(option)
            dev = status.soap_body.ValideElServicioResult
        except Exception as e:
            logger.error("Autenticador: servicio validar autenticacion fallando %s" %
                         (e,))
            dev = False
        return dev

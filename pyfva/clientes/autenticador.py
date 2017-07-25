# encoding: utf-8

'''
Created on 18 jul. 2017

@author: luis
'''
from pyfva.soap.autenticador import AutenticadorSoapServiceStub,\
    RecibaLaSolicitudDeAutenticacion, SolicitudDeAutenticacion, ValideElServicio

from datetime import datetime
import warnings
from pyfva.soap import settings


class ClienteAutenticador(object):
    """
    Permite autenticar una persona utilizando los servicios del BCCR
    """
    DEFAULT_ERROR = {
        'codigo_error': 2,
        'codigo_verificacion': 'N/D',
        'tiempo_maximo': 1,
        'id_solicitud': 0
    }

    def __init__(self,
                 negocio=settings.DEFAULT_BUSSINESS,
                 entidad=settings.DEFAULT_ENTITY):
        self.negocio = negocio
        self.entidad = entidad

    def solicitar_autenticacion(self, identificacion):
        """
        Solicita al BCCR la autenticación de la identificacion

        Params:
           identificacion: número de identificación de la persona
           negocio: número de identificación del negocio (provisto por el BCCR)
           entidad: número de identificación de la entidad (provisto por el BCCR)

        Return:
            codigo_error: Número con el código de error 1 es éxito
            codigo_verificacion: str con el código de verificación de la trasacción
            tiempo_maximo: Tiempo máximo de duración de la solicitud en segundos
            id_solicitud: Número de identificación de la solicitud

        """

        request = SolicitudDeAutenticacion.create(
            self.negocio,
            datetime.now(),
            self.entidad,
            identificacion
        )
        try:
            dev = self._solicitar_autenticacion(request)
        except:
            dev = self.DEFAULT_ERROR
        return dev

    def validar_servicio(self):
        """
        Valida si el servicio está disponible.  Retorna True si lo está o 
        False si ocurrió algún error contactando al BCCR o el servicio no está disponible
        """
        return self._validar_servicio()

    def extract_result(self, request,  result):
        try:
            data = self._extract_result(request,  result)
        except:
            data = self.DEFAULT_ERROR
        return data

    def _solicitar_autenticacion(self, request):
        stub = AutenticadorSoapServiceStub()
        options = RecibaLaSolicitudDeAutenticacion()
        options.laSolicitud = request

        status = stub.RecibaLaSolicitudDeAutenticacion(options)

        return self.extract_result(
            request, status.soap_body.RecibaLaSolicitudDeAutenticacionResult)

    def _extract_result(self, request, result):
        data = {
            'codigo_error': result.CodigoDeError,
            'codigo_verificacion': result.CodigoDeVerificacion,
            'tiempo_maximo': result.TiempoMaximoDeFirmaEnSegundos,
            'id_solicitud': result.IdDeLaSolicitud
        }
        return data

    def _validar_servicio(self):
        stub = AutenticadorSoapServiceStub()
        option = ValideElServicio()
        try:
            status = stub.ValideElServicio(option)
            dev = status.soap_body.ValideElServicioResult
        except Exception as e:
            warnings.warn("servicio de autenticacion fallando %s" %
                          (e,), RuntimeWarning)

            dev = False
        return dev

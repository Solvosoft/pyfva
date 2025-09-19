# encoding: utf-8

'''
Created on 11 de septiembre de 2025

@author: luisza
'''



from requests import HTTPError

from pyfva.conf import settings
import requests
from pyfva.constants import ERRORES_AL_SOLICITAR_FIRMA, get_text_representation

from pyfva import logger
from .core import BCCRRestClient


class RestAutenticador(BCCRRestClient):
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

    def solicitar_autenticacion(self, identificacion:str, id_funcionalidad:int=-1):
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
        logger.info({'message': f"Autenticador: Solicitar_autenticacion {identificacion}",
                     'data':identificacion, 'location': __file__})
        logger.debug({'message': "Autenticador: Solicitar_autenticacion Fin", 'data': {
            'negocio': self.negocio,
            'hora': self.get_now(),
            'entidad': self.entidad,
            'identificacion': identificacion
        }, 'location': __file__})
        try:
            response = requests.post(
                settings.BASE_REST_URL + settings.SERVICE_URLS['autenticacion'],
                json={
                        'fechaDeReferenciaDeLaEntidad': self.get_now(),
                        'codNegocio': self.negocio,
                        'idReferenciaEntidad': self.entidad,
                        'idFuncionalidad': id_funcionalidad,
                        'identificacionDelSuscriptor': identificacion
                },
                **self.get_requests_extra_headers()
            )
            response.raise_for_status()
            dev = self.extract_data(response.json())
        except HTTPError as e:
            dev = self.DEFAULT_ERROR
            logger.error({"message":"Autenticador: POST error autenticacion", 'data': e, 'location': __file__})
        logger.debug({"message":"Autenticador: Solicitar_autenticacion", 'data': dev, 'location': __file__})
        return dev


    def validar_servicio(self):
        """
        Valida si el servicio está disponible.

        :returns: True si lo está o False si ocurrió algún error contactando al BCCR o el servicio no está disponible
        """

        response = requests.get(settings.BASE_REST_URL+settings.SERVICE_URLS['valida_autenticacion'])
        response.raise_for_status()
        dev = response.json()
        logger.debug({'message':"Autenticador: validar_servicio", 'data': dev, 'location': __file__})
        return dev

    def extract_data(self, data):
        dev = {
            'codigo_error': data['codigoDeError'],
            'texto_codigo_error': get_text_representation(
                ERRORES_AL_SOLICITAR_FIRMA, data['codigoDeError']),
            'codigo_verificacion': data['codigoDeVerificacion'],
            'tiempo_maximo': data['tiempoMaximoDeFirmaEnSegundos'],
            'id_solicitud': data['idDeLaSolicitud'],
            'resumen': data['resumenDelDocumento'],
            'informacionSuscriptorDesconectado': data['informacionSuscriptorDesconectado'],
        }
        return dev
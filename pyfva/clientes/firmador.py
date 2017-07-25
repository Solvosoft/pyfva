'''
Created on 19 jul. 2017

@author: luis
'''
from pyfva.soap.firmador import FirmadorSoapServiceStub,\
    RecibaLaSolicitudDeFirmaXmlEnvelopedCoFirma, RecibaLaSolicitudDeFirmaODF,\
    RecibaLaSolicitudDeFirmaMSOffice, ValideElServicio,\
    ElSuscriptorEstaConectado, SolicitudDeFirma

from pyfva.soap import settings

from datetime import datetime
import logging

logger = logging.getLogger('pyfva')


class ClienteFirmador(object):
    """Permite firmar un documento utilizando los servicios del BCCR

    .. note:: 
        Recuerde la política del banco es *no nos llame, nosotros lo llamamos*

    :param negocio: número de identificación del negocio (provisto por el BCCR)
    :param entidad: número de identificación de la entidad (provisto por el BCCR)
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

    def firme(self, identidad, documento, formato, algoritmo_hash='Sha512', hash_doc=None, resumen=''):
        """
        Firma cualquier documento enviado distinguiendo por el parámtetro formato cual método de firma llamar

        :param identidad: Identidad del suscriptor a firmar
        :param documento: Documento a firmar en base64
        :param formato: Formato del documento, puede ser *xml*, *odf*, *msoffice*
        :param algoritmo_hash: Algoritmo utilizado para calcular el hash_doc, puede ser *sha256*, *sha384*, *sha512*
        :param hash_doc: hash del documento aplicando el algoritmo hash
        :param resumen: Información resumida para mostar al suscriptor que describe el documento

        Retorna una diccionario con los siguientes elementos, en caso de error retorna
        **DEFAULT_ERROR**.


        :returns:   
            **codigo_error:** Número con el código de error 1 es éxito

            **codigo_verificacion:** str con el código de verificación de la trasacción, se muestra al usuario

            **tiempo_maximo:** Tiempo máximo de duración de la solicitud en segundos

            **id_solicitud:** Número de identificación de la solicitud
        """

        logger.info("Firmador: firme %s %s %s" %
                    (identidad, formato, hash_doc))
        logger.debug("Firmador: firme %r" % (locals(), ))

        algoritmo_hash = algoritmo_hash.title()
        if formato == 'xml':
            dev = self.firme_xml(identidad, documento,
                                 algoritmo_hash, hash_doc, resumen)
        elif formato == 'odf':
            dev = self.firme_odf(identidad, documento,
                                 algoritmo_hash, hash_doc, resumen)
        elif formato == 'msoffice':
            dev = self.firme_msoffice(
                identidad, documento, algoritmo_hash, hash_doc, resumen)
        else:
            logger.error("Formato de documento inválido")
            dev = self.DEFAULT_ERROR

        logger.debug("Firmador: firme result %r" % (dev, ))
        return dev

    def firme_xml(self, identidad, documento, algoritmo_hash='Sha512', hash_doc=None, resumen=''):
        """
        Firma un documento XML, 

        .. note:: 

            Los parámetros exceptuando formato (no existe en este método) son idénticos que los 
            de firme, además los resultados retornados son también idénticos.
        """

        logger.info("Firmador: firme_xml %s %s" %
                    (identidad,  hash_doc))
        logger.debug("Firmador: firme_xml %r" % (locals(), ))

        request = self._construya_solicitud(
            identidad, documento, algoritmo_hash, hash_doc, resumen)
        try:
            dev = self._firme_xml(request)
        except Exception as e:
            logger.error("Firmador: firmando en xml %s" % (e, ))
            dev = self.DEFAULT_ERROR
        logger.debug("Firmador: firme_xml result %r" % (dev, ))
        return dev

    def firme_odf(self, identidad, documento, algoritmo_hash='Sha512', hash_doc=None, resumen=''):
        """
        Firma un documento del tipo ODF.

        .. note:: 

            Los parámetros exceptuando formato (no existe en este método) son idénticos que los 
            de firme, además los resultados retornados son también idénticos.
        """

        logger.info("Firmador: firme_odf %s %s" %
                    (identidad,  hash_doc))
        logger.debug("Firmador: firme_odf %r" % (locals(), ))

        request = self._construya_solicitud(
            identidad, documento, algoritmo_hash, hash_doc, resumen)
        try:
            dev = self._firme_odf(request)
        except Exception as e:
            logger.error("Firmador: firmando en odf %s" % (e,))
            dev = self.DEFAULT_ERROR

        logger.debug("Firmador: firme_odf result %r" % (dev, ))
        return dev

    def firme_msoffice(self, identidad, documento, algoritmo_hash='Sha512', hash_doc=None, resumen=''):
        """
        Firma un documento del tipo Microsoft office.

        .. note:: 

            Los parámetros exceptuando formato (no existe en este método) son idénticos que los 
            de firme, además los resultados retornados son también idénticos.
        """

        logger.info("Firmador: firme_msoffice %s %s" %
                    (identidad,  hash_doc))
        logger.debug("Firmador: firme_msoffice %r" % (locals(), ))

        request = self._construya_solicitud(
            identidad, documento, algoritmo_hash, hash_doc, resumen)
        try:
            dev = self._firme_msoffice(request)
        except Exception as e:
            logger.error("Firmador: firmando en msoffice %s" % (e, ))
            dev = self.DEFAULT_ERROR

        logger.debug("Firmador: firme_msoffice result %r" % (dev, ))
        return dev

    def suscriptor_conectado(self, identificacion):
        """Verifica si un suscriptor está conectado.

        :param identificacion: Identificación del suscriptor
        :returns: True si la tarjeta del suscriptor está conectada, False si no lo está.
        """

        dev = self._suscriptor_conectado(identificacion)
        logger.debug("Firmador: suscriptor conectado %r" % (dev, ))
        return dev

    def validar_servicio(self):
        """Verifica si el servicio está disponible

        :returns: True si el servicio está disponible, False si no lo está.
        """
        dev = self._validar_servicio()
        logger.debug("Firmador: validar servicio %r" % (dev, ))
        return dev

    def extrae_resultado(self, solicitud,  resultado):
        """Convierte la infromación obtenida del servicio SOAP a python

        :param solicitud:  Objeto de solicitud del tipo *pyfva.soap.firmador.SolicitudDeFirma*
        :param resultado: Objeto de respuesta del tipo *pyfva.soap.firmador.RecibaLaSolicitudDeFirmaXmlEnvelopedCoFirmaResult* 

        Retorna una diccionario con los siguientes elementos, en caso de error retorna
        **DEFAULT_ERROR**.


        :returns:   
            **codigo_error:** Número con el código de error 1 es éxito

            **codigo_verificacion:** str con el código de verificación de la trasacción

            **tiempo_maximo:** Tiempo máximo de duración de la solicitud en segundos

            **id_solicitud:** Número de identificación de la solicitud
        """
        try:
            data = self._extrae_resultado(solicitud,  resultado)
        except Exception as e:
            logger.error("Firmador: extrayendo resultados %s" % (e, ))
            data = self.DEFAULT_ERROR
        return data

    def _construya_solicitud(self, identidad, documento, algoritmo_hash='Sha512', hash_doc=None, resumen=''):
        request = SolicitudDeFirma.create(
            self.negocio,
            datetime.now(),
            algoritmo_hash,
            self.entidad
        )
        request.Documento = documento
        request.HashDocumento = hash_doc
        request.IdentificacionDelSuscriptor = identidad
        request.ResumenDocumento = resumen

        return request

    # Private methods
    def _extrae_resultado(self, request, result):
        data = {
            'codigo_error': result.CodigoDeError,
            'codigo_verificacion': result.CodigoDeVerificacion,
            'tiempo_maximo': result.TiempoMaximoDeFirmaEnSegundos,
            'id_solicitud': result.IdDeLaSolicitud
        }
        return data

    def _firme_xml(self, request):
        stub = FirmadorSoapServiceStub()
        options = RecibaLaSolicitudDeFirmaXmlEnvelopedCoFirma()
        options.laSolicitud = request
        status = stub.RecibaLaSolicitudDeFirmaXmlEnvelopedCoFirma(options)
        return self.extrae_resultado(request,
                                     status.soap_body.RecibaLaSolicitudDeFirmaXmlEnvelopedCoFirmaResult)

    def _firme_odf(self, request):
        stub = FirmadorSoapServiceStub()
        options = RecibaLaSolicitudDeFirmaODF()
        options.laSolicitud = request
        status = stub.RecibaLaSolicitudDeFirmaODF(options)
        return self.extrae_resultado(request,
                                     status.soap_body.RecibaLaSolicitudDeFirmaODFResult)

    def _firme_msoffice(self, request):
        stub = FirmadorSoapServiceStub()
        options = RecibaLaSolicitudDeFirmaMSOffice()
        options.laSolicitud = request
        status = stub.RecibaLaSolicitudDeFirmaMSOffice(options)
        return self.extrae_resultado(request,
                                     status.soap_body.RecibaLaSolicitudDeFirmaMSOfficeResult)

    def _suscriptor_conectado(self, identificacion):
        stub = FirmadorSoapServiceStub()
        options = ElSuscriptorEstaConectado()
        options.laIdentificacion = identificacion
        try:
            status = stub.ElSuscriptorEstaConectado(options)
            dev = status.soap_body.ElSuscriptorEstaConectadoResult
        except Exception as e:
            logger.error(
                "Firmador: Servicio de firmado fallando en usuario conectado%s" % (e, ))
            dev = False
        return dev

    def _validar_servicio(self):
        stub = FirmadorSoapServiceStub()
        option = ValideElServicio()
        try:
            status = stub.ValideElServicio(option)
            dev = status.soap_body.ValideElServicioResult
        except Exception as e:
            logger.error(
                "Firmador: Servicio de firmado fallando %s" % (e, ))
            dev = False
        return dev

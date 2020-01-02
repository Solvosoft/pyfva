'''
Created on 19 jul. 2017

@author: luis
'''
from pyfva.soap.firmador import FirmadorSoapServiceStub,\
    RecibaLaSolicitudDeFirmaXmlEnvelopedCoFirma, RecibaLaSolicitudDeFirmaODF,\
    RecibaLaSolicitudDeFirmaMSOffice, ValideElServicio,\
    ElSuscriptorEstaConectado, SolicitudDeFirma,\
    RecibaLaSolicitudDeFirmaXmlEnvelopedContraFirma, \
    RecibaLaSolicitudDeFirmaPdf, SolicitudDeFirmaPdf

from pyfva.soap import settings

from datetime import datetime
import logging
from pyfva.constants import ERRORES_AL_SOLICITAR_FIRMA, \
    get_text_representation

from pyfva import logger


class ClienteFirmador(object):
    """Permite firmar un documento utilizando los servicios del BCCR.

    Los documentos que se pueden firmar son:

    * XML: con cofirma y contrafirma
    * MSOffice: .docx, .xlsx y .pptx
    * ODF: .odt, .ods y .odp 
    * PDF: .pdf

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

    def firme(self, identidad, documento, formato, algoritmo_hash='Sha512', hash_doc=None,
              resumen='', id_funcionalidad=-1, lugar=None, razon=None):
        """
        Firma cualquier documento enviado distinguiendo por el parámtetro formato cual método de firma llamar

        :param identidad: Identidad del suscriptor a firmar
        :param documento: Documento a firmar en base64
        :param formato: Formato del documento, puede ser *xml_cofirma*, *xml_contrafirma*, *odf*, *msoffice*, *pdf*
        :param algoritmo_hash: Algoritmo utilizado para calcular el hash_doc, puede ser *sha256*, *sha384*, *sha512*
        :param hash_doc: hash del documento aplicando el algoritmo hash
        :param resumen: Información resumida para mostar al suscriptor que describe el documento
        :param id_funcionalidad: Identificación de la funcionalidad del programa externo, se usa para dar seguimiento a la operación, * No obligatorio
        :param lugar:  Lugar donde se realizó la firma (solo PDF)
        :param razon:  Razon de firma para PDF (solo PDF)

        Retorna una diccionario con los siguientes elementos, en caso de error retorna
        **DEFAULT_ERROR**.


        :returns:   
            **codigo_error:** Número con el código de error 1 es éxito

            **texto_codigo_error:** Descripción del error

            **codigo_verificacion:** str con el código de verificación de la trasacción, se muestra al usuario

            **tiempo_maximo:** Tiempo máximo de duración de la solicitud en segundos

            **id_solicitud:** Número de identificación de la solicitud
        """

        logger.info({'message': "Firmador: firme ", 'data':
            {'identity':identidad, 'format': formato, 'hash_doc': hash_doc}, 'location': __file__})
        logger.debug({'message': "Firmador: firme", 'data': repr(locals()), 'location': __file__})

        algoritmo_hash = algoritmo_hash.title()
        if formato in ['xml_cofirma', 'xml_contrafirma']:
            _type = formato.replace('xml_', '')
            dev = self.firme_xml(identidad, documento,
                                 algoritmo_hash, hash_doc, resumen,
                                 id_funcionalidad, _type)
        elif formato == 'odf':
            dev = self.firme_odf(identidad, documento,
                                 algoritmo_hash, hash_doc, resumen,
                                 id_funcionalidad)
        elif formato == 'msoffice':
            dev = self.firme_msoffice(
                identidad, documento, algoritmo_hash, hash_doc, resumen,
                id_funcionalidad)
        elif formato == 'pdf':
            dev = self.firme_pdf(
                identidad, documento, algoritmo_hash=algoritmo_hash,
                hash_doc=hash_doc, resumen=resumen,
                id_funcionalidad=id_funcionalidad,
                lugar=lugar, razon=razon)
        else:
            logger.error({'message': "Formato de documento inválido", 'data': formato, 'location': __file__})
            dev = self.DEFAULT_ERROR

        logger.debug({'message':"Firmador: firme result", 'data': dev, 'location': __file__})
        return dev

    def firme_xml(self, identidad, documento, algoritmo_hash='Sha512', hash_doc=None, resumen='',
                  id_funcionalidad=-1, _type='cofirma'):
        """
        Firma un documento XML, 

        .. note:: 

            Los parámetros exceptuando formato (no existe en este método) son idénticos que los 
            de firme, además los resultados retornados son también idénticos.
        """

        logger.info({'message': "Firmador: firme_xml", 'data':{
                    'type':_type, 'identity': identidad, 'hash_doc': hash_doc},
                     'location': __file__})
        logger.debug({'message': "Firmador: firme_xml", 'data': repr(locals()), 'location': __file__})

        request = self._construya_solicitud(
            identidad, documento, algoritmo_hash, hash_doc, resumen, id_funcionalidad)
        try:
            dev = self._firme_xml(request, _type)
        except Exception as e:
            logger.error({'message': "Firmador: firmando en xml", 'data':
                {'type': _type, 'data':e}, 'location': __file__})
            dev = self.DEFAULT_ERROR
        logger.debug({'message':"Firmador: firme_xml result",
                      'data': {'type':_type, 'data':dev}, 'location': __file__})
        return dev

    def firme_odf(self, identidad, documento, algoritmo_hash='Sha512', hash_doc=None, resumen='', id_funcionalidad=-1):
        """
        Firma un documento del tipo ODF.

        .. note:: 

            Los parámetros exceptuando formato (no existe en este método) son idénticos que los 
            de firme, además los resultados retornados son también idénticos.
        """

        logger.info({'message':"Firmador: firme_odf", 'data':
            {'identity': identidad, 'hash_doc':  hash_doc}, 'location': __file__})
        logger.debug({'message':"Firmador: firme_odf", 'data': repr(locals()), 'location': __file__})

        request = self._construya_solicitud(
            identidad, documento, algoritmo_hash, hash_doc, resumen, id_funcionalidad)
        try:
            dev = self._firme_odf(request)
        except Exception as e:
            logger.error({'message':"Firmador: firmando en odf", 'data':e, 'location': __file__})
            dev = self.DEFAULT_ERROR

        logger.debug({'message': "Firmador: firme_odf result", 'data': dev, 'location': __file__})
        return dev

    def firme_msoffice(self, identidad, documento, algoritmo_hash='Sha512', hash_doc=None, resumen='', id_funcionalidad=-1):
        """
        Firma un documento del tipo Microsoft office.

        .. note:: 

            Los parámetros exceptuando formato (no existe en este método) son idénticos que los 
            de firme, además los resultados retornados son también idénticos.
        """

        logger.info({'message': "Firmador: firme_msoffice", 'data':
            {'identity': identidad, 'hash_doc': hash_doc}, 'location': __file__})
        logger.debug({'message': "Firmador: firme_msoffice", 'data': repr(locals()), 'location': __file__})

        request = self._construya_solicitud(
            identidad, documento, algoritmo_hash, hash_doc, resumen, id_funcionalidad)
        try:
            dev = self._firme_msoffice(request)
        except Exception as e:
            logger.error({'message': "Firmador: firmando en msoffice", 'data': e, 'location': __file__})
            dev = self.DEFAULT_ERROR

        logger.debug({'message': "Firmador: firme_msoffice result", 'data': dev, 'location': __file__})
        return dev

    def firme_pdf(self, identidad, documento, algoritmo_hash='Sha512', hash_doc=None, resumen='',
                  id_funcionalidad=-1, lugar=None, razon=None):
        """
        Firma un documento del tipo PDF.

        .. note:: 

            Los parámetros exceptuando formato (no existe en este método) son idénticos que los 
            de firme, además los resultados retornados son también idénticos.
        """

        logger.info({'message': "Firmador: firme_pdf", 'data':
                     {'identity': identidad, 'hash_doc': hash_doc}, 'location': __file__})
        logger.debug({'message': "Firmador: firme_pdf", 'data':repr(locals()), 'location': __file__})

        request = self._construya_solicitud_pdf(
            identidad, documento, algoritmo_hash, hash_doc, resumen, id_funcionalidad,
            lugar, razon)
        try:
            dev = self._firme_pdf(request)
        except Exception as e:
            logger.error({'message': "Firmador: firmando en pdf", 'data':e, 'location': __file__})
            dev = self.DEFAULT_ERROR

        logger.debug({'message': "Firmador: firme_pdf result", 'data': dev, 'location': __file__})
        return dev

    def suscriptor_conectado(self, identificacion):
        """Verifica si un suscriptor está conectado.

        :param identificacion: Identificación del suscriptor
        :returns: True si la tarjeta del suscriptor está conectada, False si no lo está.
        """

        dev = self._suscriptor_conectado(identificacion)
        logger.debug({'message': "Firmador: suscriptor conectado", 'data': dev, 'location': __file__})
        return dev

    def validar_servicio(self):
        """Verifica si el servicio está disponible

        :returns: True si el servicio está disponible, False si no lo está.
        """
        dev = self._validar_servicio()
        logger.debug({'message': "Firmador: validar servicio", 'data': dev, 'location': __file__})
        return dev

    def extrae_resultado(self, solicitud,  resultado):
        """Convierte la infromación obtenida del servicio SOAP a python

        :param solicitud:  Objeto de solicitud del tipo *pyfva.soap.firmador.SolicitudDeFirma*
        :param resultado: Objeto de respuesta del tipo *pyfva.soap.firmador.RecibaLaSolicitudDeFirmaXmlEnvelopedCoFirmaResult* 

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
            logger.error({'message': "Firmador: extrayendo resultados %r", 'data': e, 'location': __file__})
            data = self.DEFAULT_ERROR
        return data

    def _construya_solicitud(self, identidad, documento,
                             algoritmo_hash='Sha512', hash_doc=None, resumen='', id_funcionalidad=-1):
        request = SolicitudDeFirma.create(
            self.negocio,
            self.get_now(),
            algoritmo_hash,
            id_funcionalidad,
            self.entidad
        )
        request.Documento = documento
        request.HashDocumento = hash_doc
        request.IdentificacionDelSuscriptor = identidad
        request.IdFuncionalidad = id_funcionalidad
        request.ResumenDocumento = resumen

        return request

    def _construya_solicitud_pdf(self, identidad, documento, algoritmo_hash='Sha512',
                                 hash_doc=None, resumen='', id_funcionalidad=-1,
                                 lugar=None, razon=None):
        request = SolicitudDeFirmaPdf.create(
            self.negocio,
            self.get_now(),
            algoritmo_hash,
            id_funcionalidad,
            self.entidad
        )
        request.Documento = documento
        request.HashDocumento = hash_doc
        request.IdentificacionDelSuscriptor = identidad
        request.IdFuncionalidad = id_funcionalidad
        request.ResumenDocumento = resumen
        if lugar:
            request.Lugar = lugar
        if razon:
            request.RazonDeFirma = razon

        return request

    # Private methods

    def _extrae_resultado(self, request, result):
        data = {
            'codigo_error': result.CodigoDeError,
            'texto_codigo_error': get_text_representation(
                ERRORES_AL_SOLICITAR_FIRMA, result.CodigoDeError),
            'codigo_verificacion': result.CodigoDeVerificacion,
            'tiempo_maximo': result.TiempoMaximoDeFirmaEnSegundos,
            'id_solicitud': result.IdDeLaSolicitud
        }
        return data

    def _firme_xml(self, request, _type):
        stub = FirmadorSoapServiceStub()
        if _type == 'cofirma':
            options = RecibaLaSolicitudDeFirmaXmlEnvelopedCoFirma()
            options.laSolicitud = request
            status = stub.RecibaLaSolicitudDeFirmaXmlEnvelopedCoFirma(options)
            return self.extrae_resultado(request,
                                         status.soap_body.RecibaLaSolicitudDeFirmaXmlEnvelopedCoFirmaResult)
        elif _type == 'contrafirma':
            options = RecibaLaSolicitudDeFirmaXmlEnvelopedContraFirma()
            options.laSolicitud = request
            status = stub.RecibaLaSolicitudDeFirmaXmlEnvelopedContraFirma(
                options)
            return self.extrae_resultado(request,
                                         status.soap_body.RecibaLaSolicitudDeFirmaXmlEnvelopedContraFirmaResult)

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

    def _firme_pdf(self, request):
        stub = FirmadorSoapServiceStub()
        options = RecibaLaSolicitudDeFirmaPdf()
        options.laSolicitud = request
        status = stub.RecibaLaSolicitudDeFirmaPdf(options)
        return self.extrae_resultado(request,
                                     status.soap_body.RecibaLaSolicitudDeFirmaPdfResult)

    def _suscriptor_conectado(self, identificacion):
        stub = FirmadorSoapServiceStub()
        options = ElSuscriptorEstaConectado()
        options.laIdentificacion = identificacion
        try:
            status = stub.ElSuscriptorEstaConectado(options)
            dev = status.soap_body.ElSuscriptorEstaConectadoResult
        except Exception as e:
            logger.error({'message':
                "Firmador: Servicio de firmado fallando en usuario conectado",
                         'data': e, 'location': __file__})
            dev = False
        return dev

    def _validar_servicio(self):
        stub = FirmadorSoapServiceStub()
        option = ValideElServicio()
        try:
            status = stub.ValideElServicio(option)
            dev = status.soap_body.ValideElServicioResult
        except Exception as e:
            logger.error({'message':
                "Firmador: Servicio de firmado fallando", 'data': e, 'location': __file__})
            dev = False
        return dev

'''
Created on 6 sept. 2020

@author: luis
'''
from pyfva.soap.sellador import SolicitudDeFirma, SelladorElectronicoConControlDeLlaveSoapServiceStub, \
    ValideElServicio, RecibaLaSolicitudDeSelladoElectronicoOdf, RecibaLaSolicitudDeSelladoElectronicoPdf, \
    RecibaLaSolicitudDeSelladoElectronicoMSOffice, RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma, \
    RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma, SolicitudDeFirmaPdf

from pyfva.soap import settings

from datetime import datetime

from pyfva.constants import ERRORES_AL_SOLICITAR_SELLO, \
    get_text_representation

from pyfva import logger


class ClienteSellador(object):
    """Permite firmar con sello electrónico un documento utilizando los servicios del BCCR.

    Los documentos que se pueden firmar son:

    * XML: con cofirma y contrafirma
    * MSOffice: .docx, .xlsx y .pptx
    * ODF: .odt, .ods y .odp 
    * PDF: .pdf

    .. note:: El número de entidad no se usa en sello electrónico
    
    :param negocio: número de identificación del negocio (provisto por el BCCR)
    :param entidad: número de identificación de la entidad (provisto por el BCCR)
    """
    HASH_IDS = {
        1: 'sha256',
        2: 'sha384',
        3: 'sha512'
    }

    DEFAULT_ERROR = {
        'codigo_error': 1,
        'texto_codigo_error': get_text_representation(ERRORES_AL_SOLICITAR_SELLO, 1),
        'fue_exitosa': False,
        'documento': None,
        'hash_documento': None,
        'id_algoritmo_hash': 'sha256'
    }

    def __init__(self, negocio=settings.DEFAULT_BUSSINESS, entidad=settings.DEFAULT_ENTITY):
        self.negocio = negocio
        self.entidad = entidad

    def get_now(self):
        return datetime.now()

    def firme(self, documento, formato, algoritmo_hash='Sha512', hash_doc=None,
              id_funcionalidad=-1, lugar=None, razon=None):
        """
        Firma con sello electrónico cualquier documento enviado distinguiendo por el parámtetro formato cual método de firma llamar

        :param documento: Documento a firmar en base64
        :param formato: Formato del documento, puede ser *xml_cofirma*, *xml_contrafirma*, *odf*, *msoffice*, *pdf*
        :param algoritmo_hash: Algoritmo utilizado para calcular el hash_doc, puede ser *sha256*, *sha384*, *sha512*
        :param hash_doc: hash del documento aplicando el algoritmo hash
        :param id_funcionalidad: Identificación de la funcionalidad del programa externo, se usa para dar seguimiento a la operación, * No obligatorio
        :param lugar:  Lugar donde se realizó la firma (solo PDF)
        :param razon:  Razon de firma para PDF (solo PDF)

        Retorna una diccionario con los siguientes elementos, en caso de error retorna
        **DEFAULT_ERROR**.


        :returns:   
            **codigo_error:** Número con el código de error 1 es éxito

            **texto_codigo_error:** Descripción del error

            **fue_exitosa:** Verdadero si se pudo sellar, falso si hay un error

            **documento:** Documento en base64 si fue_exitosa True

            **hash_documento:** hash del documento en base64 si fue_exitosa True

            **id_algoritmo_hash:** algoritmo con el que se calculó la suma hash opciones: sha256, sha384, sha512
        """

        logger.info({'message': "Sellador: firme ", 'data':
            {'format': formato, 'hash_doc': hash_doc}, 'location': __file__})
        logger.debug({'message': "Sellador: firme", 'data': repr(locals()), 'location': __file__})

        algoritmo_hash = algoritmo_hash.title()
        if formato in ['xml_cofirma', 'xml_contrafirma']:
            _type = formato.replace('xml_', '')
            dev = self.firme_xml(documento, algoritmo_hash, hash_doc, id_funcionalidad, _type)
        elif formato == 'odf':
            dev = self.firme_odf(documento, algoritmo_hash, hash_doc, id_funcionalidad)
        elif formato == 'msoffice':
            dev = self.firme_msoffice(documento, algoritmo_hash, hash_doc, id_funcionalidad)
        elif formato == 'pdf':
            dev = self.firme_pdf(documento, algoritmo_hash=algoritmo_hash,
                                 hash_doc=hash_doc, id_funcionalidad=id_funcionalidad, lugar=lugar, razon=razon)
        else:
            logger.error({'message': "Formato de documento inválido", 'data': formato, 'location': __file__})
            dev = self.DEFAULT_ERROR

        logger.debug({'message': "Sellador: firme result", 'data': dev, 'location': __file__})
        return dev

    def firme_xml(self, documento, algoritmo_hash='Sha512', hash_doc=None, id_funcionalidad=-1, _type='cofirma'):
        """
        Firma un documento XML, 

        .. note:: 

            Los parámetros exceptuando formato (no existe en este método) son idénticos que los 
            de firme, además los resultados retornados son también idénticos.
        """

        logger.info({'message': "Sellador: firme_xml", 'data': {'type': _type, 'hash_doc': hash_doc},
                     'location': __file__})
        logger.debug({'message': "Sellador: firme_xml", 'data': repr(locals()), 'location': __file__})

        request = self._construya_solicitud(documento, algoritmo_hash, hash_doc, id_funcionalidad)
        try:
            dev = self._firme_xml(request, _type)
        except Exception as e:
            logger.error({'message': "Sellador: firmando en xml", 'data': {'type': _type, 'data': e},
                          'location': __file__})
            dev = self.DEFAULT_ERROR
        logger.debug({'message': "Sellador: firme_xml result", 'data': {'type': _type, 'data': dev},
                      'location': __file__})
        return dev

    def firme_odf(self, documento, algoritmo_hash='Sha512', hash_doc=None, id_funcionalidad=-1):
        """
        Firma un documento del tipo ODF.

        .. note:: 

            Los parámetros exceptuando formato (no existe en este método) son idénticos que los 
            de firme, además los resultados retornados son también idénticos.
        """

        logger.info({'message': "Sellador: firme_odf", 'data': {'hash_doc': hash_doc},
                     'location': __file__})
        logger.debug({'message': "Sellador: firme_odf", 'data': repr(locals()), 'location': __file__})

        request = self._construya_solicitud(documento, algoritmo_hash, hash_doc, id_funcionalidad)
        try:
            dev = self._firme_odf(request)
        except Exception as e:
            logger.error({'message': "Sellador: firmando en odf", 'data': e, 'location': __file__})
            dev = self.DEFAULT_ERROR

        logger.debug({'message': "Sellador: firme_odf result", 'data': dev, 'location': __file__})
        return dev

    def firme_msoffice(self, documento, algoritmo_hash='Sha512', hash_doc=None, id_funcionalidad=-1):
        """
        Firma un documento del tipo Microsoft office.

        .. note:: 

            Los parámetros exceptuando formato (no existe en este método) son idénticos que los 
            de firme, además los resultados retornados son también idénticos.
        """

        logger.info({'message': "Sellador: firme_msoffice", 'data': {'hash_doc': hash_doc},
                     'location': __file__})
        logger.debug({'message': "Sellador: firme_msoffice", 'data': repr(locals()), 'location': __file__})

        request = self._construya_solicitud(documento, algoritmo_hash, hash_doc, id_funcionalidad)
        try:
            dev = self._firme_msoffice(request)
        except Exception as e:
            logger.error({'message': "Sellador: firmando en msoffice", 'data': e, 'location': __file__})
            dev = self.DEFAULT_ERROR

        logger.debug({'message': "Sellador: firme_msoffice result", 'data': dev, 'location': __file__})
        return dev

    def firme_pdf(self, documento, algoritmo_hash='Sha512', hash_doc=None, id_funcionalidad=-1,
                  lugar=None, razon=None):
        """
        Firma un documento del tipo PDF.

        .. note:: 

            Los parámetros exceptuando formato (no existe en este método) son idénticos que los 
            de firme, además los resultados retornados son también idénticos.
        """

        logger.info({'message': "Sellador: firme_pdf", 'data': {'hash_doc': hash_doc}, 'location': __file__})
        logger.debug({'message': "Sellador: firme_pdf", 'data': repr(locals()), 'location': __file__})

        request = self._construya_solicitud_pdf(documento, algoritmo_hash, hash_doc, id_funcionalidad,
                                                lugar, razon)
        try:
            dev = self._firme_pdf(request)
        except Exception as e:
            logger.error({'message': "Sellador: firmando en pdf", 'data': e, 'location': __file__})
            dev = self.DEFAULT_ERROR

        logger.debug({'message': "Sellador: firme_pdf result", 'data': dev, 'location': __file__})
        return dev

    def validar_servicio(self):
        """Verifica si el servicio está disponible

        :returns: True si el servicio está disponible, False si no lo está.
        """
        dev = self._validar_servicio()
        logger.debug({'message': "Sellador: validar servicio", 'data': dev, 'location': __file__})
        return dev

    def extrae_resultado(self, solicitud, resultado):
        """Convierte la infromación obtenida del servicio SOAP a python

        :param solicitud:  Objeto de solicitud del tipo *pyfva.soap.firmador.SolicitudDeFirma*
        :param resultado: Objeto de respuesta del tipo *pyfva.soap.firmador.RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirmaResult* 

        Retorna una diccionario con los siguientes elementos, en caso de error retorna
        **DEFAULT_ERROR**.


        :returns:   
            **codigo_error:** Número con el código de error 1 es éxito

            **texto_codigo_error:** Descripción del error

            **fue_exitosa:** Verdadero si se pudo sellar, falso si hay un error

            **documento:** Documento en base64 si fue_exitosa True

            **hash_documento:** hash del documento en base64 si fue_exitosa True

            **id_algoritmo_hash:** algoritmo con el que se calculó la suma hash opciones: sha256, sha384, sha512
        """
        try:
            data = self._extrae_resultado(solicitud, resultado)
        except Exception as e:
            logger.error({'message': "Sellador: extrayendo resultados %r", 'data': e, 'location': __file__})
            data = self.DEFAULT_ERROR
        return data

    def _construya_solicitud(self, documento, algoritmo_hash='Sha512', hash_doc=None,  id_funcionalidad=-1):
        request = SolicitudDeFirma.create(self.get_now(), algoritmo_hash, self.negocio, id_funcionalidad)
        request.Documento = documento
        request.HashDocumento = hash_doc
        request.IdFuncionalidad = id_funcionalidad
        return request

    def _construya_solicitud_pdf(self, documento, algoritmo_hash='Sha512',
                                 hash_doc=None, id_funcionalidad=-1,
                                 lugar=None, razon=None):
        request = SolicitudDeFirmaPdf.create(
            self.negocio,
            self.get_now(),
            algoritmo_hash,
            id_funcionalidad
        )
        request.Documento = documento
        request.HashDocumento = hash_doc
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
                ERRORES_AL_SOLICITAR_SELLO, result.CodigoDeError),
            'fue_exitosa': result.FueExitosa,
            'documento': result.DocumentoFirmado,
            'hash_documento': result.HashDocumentoFirmado,
            'id_algoritmo_hash': self.HASH_IDS[result.IDAlgoritmoHashDocumentoFirmado]
        }

        return data

    def _firme_xml(self, request, _type):
        stub = SelladorElectronicoConControlDeLlaveSoapServiceStub()
        if _type == 'cofirma':
            options = RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma()
            options.laSolicitud = request
            status = stub.RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma(options)
            return self.extrae_resultado(request,
                                         status.soap_body.RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirmaResult)
        elif _type == 'contrafirma':
            options = RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma()
            options.laSolicitud = request
            status = stub.RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma(
                options)
            return self.extrae_resultado(request,
                                         status.soap_body.RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirmaResult)

    def _firme_odf(self, request):
        stub = SelladorElectronicoConControlDeLlaveSoapServiceStub()
        options = RecibaLaSolicitudDeSelladoElectronicoOdf()
        options.laSolicitud = request
        status = stub.RecibaLaSolicitudDeSelladoElectronicoOdf(options)
        return self.extrae_resultado(request,
                                     status.soap_body.RecibaLaSolicitudDeSelladoElectronicoOdfResult)

    def _firme_msoffice(self, request):
        stub = SelladorElectronicoConControlDeLlaveSoapServiceStub()
        options = RecibaLaSolicitudDeSelladoElectronicoMSOffice()
        options.laSolicitud = request
        status = stub.RecibaLaSolicitudDeSelladoElectronicoMSOffice(options)
        return self.extrae_resultado(request,
                                     status.soap_body.RecibaLaSolicitudDeSelladoElectronicoMSOfficeResult)

    def _firme_pdf(self, request):
        stub = SelladorElectronicoConControlDeLlaveSoapServiceStub()
        options = RecibaLaSolicitudDeSelladoElectronicoPdf()
        options.laSolicitud = request
        status = stub.RecibaLaSolicitudDeSelladoElectronicoPdf(options)
        return self.extrae_resultado(request,
                                     status.soap_body.RecibaLaSolicitudDeSelladoElectronicoPdfResult)

    def _validar_servicio(self):
        stub = SelladorElectronicoConControlDeLlaveSoapServiceStub()
        option = ValideElServicio()
        try:
            status = stub.ValideElServicio(option)
            dev = status.soap_body.ValideElServicioResult
        except Exception as e:
            logger.error({'message': "Sellador: Servicio de firmado fallando", 'data': e,
                          'location': __file__})
            dev = False
        return dev

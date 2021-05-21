'''
Created on 19 jul. 2017

@author: luis
'''

from pyfva.soap.validador_certificado import ValideElServicio as ValideServicioCertificado,\
    ValidadorDeCertificadoSoapServiceStub,\
    SoliciteLaValidacionDelCertificadoDeAutenticacion
from pyfva.soap.validador_documento_v2 import ValideElServicio as ValideServicioDocumento,\
    ValideElDocumentoXmlEnvelopedCoFirma,\
    ValideElDocumentoXmlEnvelopedContraFirma, ValideElDocumentoMSOffice, ValideElDocumentoOdf, \
    ValideElDocumentoPdf

from pyfva.soap import settings
from pyfva.constants import get_text_representation, ERRORES_VALIDA_CERTIFICADO,\
    ERRORES_VALIDAR_ODF, ERRORES_VALIDAR_MSOFFICE,\
    ERRORES_VALIDAR_XMLCONTRAFIRMA, ERRORES_VALIDAR_XMLCOFIRMA,\
    ERRORES_VALIDAR_PDF
import traceback

from pyfva import logger
from pyfva.soap.validador_documento_v2 import ValidadorDeDocumentosSoapServiceStub


class ClienteValidador(object):
    """Permite validar una firma o un documento utilizando los servicios del BCCR

    Los documentos que se pueden validar son:

    * Certificados digitales (CA nacional)
    * XML: con cofirma y contrafirma
    * MSOffice: .docx, .xlsx y .pptx
    * ODF: .odt, .ods y .odp 
    * PDF: .pdf

    .. note:: 
        Los parámetros negocio y entidad de momento no son requeridos, pero puede que en un futuro cercano
        lo sean, por lo que se recomienda suministrarlos.

    :param negocio: número de identificación del negocio (provisto por el BCCR)
    :param entidad: número de identificación de la entidad (provisto por el BCCR)
    """
    DEFAULT_CERTIFICATE_ERROR = {
        'codigo_error': 1,
        'texto_codigo_error': get_text_representation(
            ERRORES_VALIDA_CERTIFICADO, 1),
        'exitosa': False,
        'certificado': None

    }

    def DEFAULT_DOCUMENT_ERROR(self, ERRORES_VALIDA):
        return {
            'exitosa': False,
            'codigo_error': 1,
            'texto_codigo_error': get_text_representation(ERRORES_VALIDA, 1),
            'advertencias': None,
            'errores_encontrados': None,
            'firmantes': None,
        }

    def __init__(self,
                 negocio=settings.DEFAULT_BUSSINESS,
                 entidad=settings.DEFAULT_ENTITY):
        self.negocio = negocio
        self.entidad = entidad

    def validar_documento(self, documento, formato):
        """Valida si el documento está firmado correctamente.

        :param documento: documento xml en base64
        :param formato: tipo de documento a validar (cofirma, contrafirma, msoffice, odf).

        Retorna una diccionario con los siguientes elementos, en caso de error retorna
        **DEFAULT_DOCUMENT_ERROR**.

        .. note:: 
            Observe que en caso de no ser exitosa la operación los atributos 'advertencias', 'errores_encontrados' y 'firmantes' retornarán None

        :returns:   
            **codigo_error**: Es 0 si el resultado fue exitoso, 1 si existe algún error.

            **texto_codigo_error**:  Texto de información sobre el código de error.

            **exitosa**: La transacción fue exitosa.

            **firmas**: Listado de firmas en el documento.

                - es_valida: La firma encontrada es válida.
                - es_avanzada: Es una firma avanzada.
                - error: Ha ocurrido un error al validar la firma.
                - detalle_de_error: Texto de detalle del error encontrado si existe.
                - garantia_de_integridad_y_autenticidad: La firma garantiza la integridad y autenticidad del documento
                - garantia_de_validez_tiempo: Datos de la garantía del tiempo.
                - detalle: Detalle de la firma.
                - autoria_del_firmante: La firma garantiza la autoría del firmante

            **resumen**: Resumen de resultados de validación del documento, contiene los elementos
                'integridad', 'jerarquia_de_confianza', 'vigencia', 'tipo_de_certificado', 'revocacion', 'fecha_de_firma'
                Cada uno de los elementos tiene los siguientes campos ('estado', 'se_evalua', 'respuesta', 'codigo')
            **errores**: Errores encontrados al validar el documento
        """
        logger.debug({'message':"Validador: validar_documento", 'data':
            {'format': formato, 'data': repr(locals())}, 'location': __file__})
        try:

            if formato == 'cofirma':
                dev = self._validar_documento_cofirma(documento)
            elif formato == 'contrafirma':
                dev = self._validar_documento_contrafirma(documento)
            elif formato == 'msoffice':
                dev = self._validar_documento_msoffice(documento)
            elif formato == 'odf':
                dev = self._validar_documento_odf(documento)
            elif formato == 'pdf':
                dev = self._validar_documento_pdf(documento)
            else:
                logger.error({'message':"Validador: validando documento", 'data':
                    {'format': formato,
                    'message':"No existe formato especificado"}, 'location': __file__})
                dev = self.DEFAULT_DOCUMENT_ERROR(ERRORES_VALIDAR_XMLCOFIRMA)
        except Exception as e:
            logger.error({'message':"Validador: validando documento",
                         'data': {'format': formato, 'message':  e}, 'location': __file__})
            dev = self.DEFAULT_DOCUMENT_ERROR(ERRORES_VALIDAR_XMLCOFIRMA)

        logger.info({'message': "Validador: validar_documento", 'data':
            {'format': formato, 'result': dev}, 'location': __file__})
        return dev

    def validar_certificado_autenticacion(self, certificado):
        """Valida si el certificado de autenticación es válido y no está revocado.

        :param certificado: Certificado en base64

        Retorna una diccionario con los siguientes elementos, en caso de error retorna
        **DEFAULT_CERTIFICATE_ERROR**.

        :returns:   
            **codigo_error:** Número con el código de error 0 es éxito

            **texto_codigo_error:** Descripción del error

            **exitosa:** True si fue exitosa, False si no lo fue

            **certificado:** Si la operación no fue exitosa retorna None, si lo fue retorna un diccionario con:
                **identificacion:** Número de identificación del suscriptor dueño del certificado

                **nombre:**  Nombre completo del suscriptor dueño del certificado

                **inicio_vigencia:** Fecha de inicio del vigencia del certificado

                **fin_vigencia:** Fecha de finalización de la vigencia del certificado
        """

        logger.debug({'message':
            "Validador: validar_certificado_autenticacion", 'data': repr(locals()),
                      'location': __file__})
        try:
            dev = self._validar_certificado_autenticacion(certificado)
        except Exception as e:
            logger.error({'message': "Validador: validando certificado",
                          'data': e, 'location': __file__})
            dev = self.DEFAULT_CERTIFICATE_ERROR

        logger.info({'message':
            "Validador: validar_certificado_autenticacion result ", 'data': dev, 'location': __file__})
        return dev

    def validar_servicio(self, servicio):
        """Valida si el servicio está disponible.  

        :param servicio: tipo de servicio a validar, puede ser 'certificado' o 'documento'
        :returns: True si lo está o False si ocurrió algún error contactando al BCCR o el servicio no está disponible
        """
        dev = False
        if servicio.lower() == 'certificado':
            dev = self._validar_servicio_certificado()
        elif servicio.lower() == 'documento':
            dev = self._validar_servicio_documento()

        logger.info({'message': "Validador: Validar servicio",
                     'data': {'servicio':servicio, 'result':dev}, 'location': __file__})
        return dev

    # Private methods

    def _validar_documento_cofirma(self, documento):
        stub = ValidadorDeDocumentosSoapServiceStub()
               
        options = ValideElDocumentoXmlEnvelopedCoFirma()
        options.elDocumento = documento
        try:
            status = stub.ValideElDocumentoXmlEnvelopedCoFirma(options)
            dev = self._extract_documento(
                status.soap_body.ValideElDocumentoXmlEnvelopedCoFirmaResult,
                ERRORES_VALIDAR_XMLCOFIRMA)
        except Exception as e:
            logger.error({'message':"Validador: validando  cofirma", 'data': e, 'location': __file__})
            dev = self.DEFAULT_DOCUMENT_ERROR(ERRORES_VALIDAR_XMLCOFIRMA)
            dev['extrar_error'] = str(e)
        return dev

    def _validar_documento_contrafirma(self, documento):
        stub = ValidadorDeDocumentosSoapServiceStub()
        options = ValideElDocumentoXmlEnvelopedContraFirma()
        options.elDocumento = documento
        try:
            status = stub.ValideElDocumentoXmlEnvelopedContraFirma(options)
            dev = self._extract_documento(
                status.soap_body.ValideElDocumentoXmlEnvelopedContraFirmaResult,
                ERRORES_VALIDAR_XMLCONTRAFIRMA)
        except Exception as e:
            traceback.print_exc()
            logger.error({'message':"Validador: validando contrafirma", 'data': e, 'location': __file__})
            dev = self.DEFAULT_DOCUMENT_ERROR(ERRORES_VALIDAR_XMLCONTRAFIRMA)
            dev['extrar_error'] = str(e)
        return dev

    def _validar_documento_msoffice(self, documento):
        stub = ValidadorDeDocumentosSoapServiceStub()
        options = ValideElDocumentoMSOffice()
        options.elDocumento = documento
        try:
            status = stub.ValideElDocumentoMSOffice(options)
            dev = self._extract_documento(
                status.soap_body.ValideElDocumentoMSOfficeResult,
                ERRORES_VALIDAR_MSOFFICE)
        except Exception as e:
            logger.error({'message':"Validador: validando  MSOffice",
                         'data': e, 'location': __file__})
            dev = self.DEFAULT_DOCUMENT_ERROR(ERRORES_VALIDAR_MSOFFICE)
            dev['extrar_error'] = str(e)
        return dev

    def _validar_documento_odf(self, documento):
        stub = ValidadorDeDocumentosSoapServiceStub()
        options = ValideElDocumentoOdf()
        options.elDocumento = documento
        try:
            status = stub.ValideElDocumentoOdf(options)
            dev = self._extract_documento(
                status.soap_body.ValideElDocumentoOdfResult,
                ERRORES_VALIDAR_ODF)
        except Exception as e:
            logger.error({'message':"Validador: validando  ODF", 'data':e, 'location': __file__})
            dev = self.DEFAULT_DOCUMENT_ERROR(ERRORES_VALIDAR_ODF)
            dev['extrar_error'] = str(e)

        return dev

    def _validar_documento_pdf(self, documento):
        stub = ValidadorDeDocumentosSoapServiceStub()
        options = ValideElDocumentoPdf()
        options.elDocumentoPdf = documento
        try:
            status = stub.ValideElDocumentoPdf(options)
            dev = self._extract_documento(
                status.soap_body.ValideElDocumentoPdfResult,
                ERRORES_VALIDAR_PDF)
        except Exception as e:
            logger.error({'message':"Validador: validando  PDF", 'data': e, 'location': __file__})
            dev = self.DEFAULT_DOCUMENT_ERROR(ERRORES_VALIDAR_PDF)
            dev['extrar_error'] = str(e)
        return dev

    def _extract_firma_detalle(self, Detalle):
        dev = {
            'integridad': None,
            'jerarquia_de_confianza': None,
            'vigencia': None,
            'tipo_de_certificado': None,
            'revocacion': None,
            'fecha_de_firma': None
        }

        if Detalle.Integridad:
            dev['integridad']={
                'estado': Detalle.Integridad.EstadoRespuesta,
                'se_evalua': Detalle.Integridad.SeEvalua,
                'respuesta': Detalle.Integridad.Respuesta or '',
                'codigo': Detalle.Integridad.CodigoRespuesta
            }
        if Detalle.JerarquiaDeConfianza:
            dev['jerarquia_de_confianza'] = {
                'estado': Detalle.JerarquiaDeConfianza.EstadoRespuesta,
                'se_evalua': Detalle.JerarquiaDeConfianza.SeEvalua,
                'respuesta': Detalle.JerarquiaDeConfianza.Respuesta or '',
                'codigo': Detalle.JerarquiaDeConfianza.CodigoRespuesta
                
            }
        if Detalle.Vigencia:
            dev['vigencia'] = {
                'estado': Detalle.Vigencia.EstadoRespuesta,
                'se_evalua': Detalle.Vigencia.SeEvalua,
                'respuesta': Detalle.Vigencia.Respuesta or '',
                'codigo': Detalle.Vigencia.CodigoRespuesta
            }
        if Detalle.TipoDeCertificado:
            dev['tipo_de_certificado'] = {
                'estado': Detalle.TipoDeCertificado.EstadoRespuesta,
                'se_evalua': Detalle.TipoDeCertificado.SeEvalua,
                'respuesta': Detalle.TipoDeCertificado.Respuesta or '',
                'codigo': Detalle.TipoDeCertificado.CodigoRespuesta
            }
        if Detalle.Revocacion:
            dev['revocacion'] = {
                'estado': Detalle.Revocacion.EstadoRespuesta,
                'se_evalua': Detalle.Revocacion.SeEvalua,
                'respuesta': Detalle.Revocacion.Respuesta or '',
                'codigo': Detalle.Revocacion.CodigoRespuesta
            }
        if Detalle.FechaOficialDeLaFirma:
            dev['fecha_de_firma'] = {
                'estado': Detalle.FechaOficialDeLaFirma.EstadoRespuesta,
                'se_evalua': Detalle.FechaOficialDeLaFirma.SeEvalua,
                'respuesta': Detalle.FechaOficialDeLaFirma.Respuesta or '',
                'codigo': Detalle.FechaOficialDeLaFirma.CodigoRespuesta,
                'fecha_de_estama': Detalle.FechaOficialDeLaFirma.FechaDeLaEstamaDeTiempo
            }
        return dev
    
    def _extract_firmas(self, Firma):
        dev = {
          'es_valida': Firma.EsValida,
          'es_avanzada': Firma.EsAvanzada,
          'error': Firma.OcurrioUnError,
          'detalle_de_error': Firma.DetalleDelError or '',
          'garantia_de_integridad_y_autenticidad':  Firma.GarantiaDeIntegridadYAutenticidad,
          'garantia_de_validez_tiempo': [],
          'detalle': [],
          'autoria_del_firmante': None,
        }
        if Firma.GarantiaDeValidezEnElTiempo:
            dev['garantia_de_validez_tiempo'].append(Firma.GarantiaDeValidezEnElTiempo.Resultado)
            dev['garantia_de_validez_tiempo'].append(Firma.GarantiaDeValidezEnElTiempo.MensajeDeAdvertencia or '')

        if Firma.AutoriaDelFirmante:
            dev['autoria_del_firmante'] = {
                'nombre': Firma.AutoriaDelFirmante.Nombre,
                'identificacion': Firma.AutoriaDelFirmante.Identificacion,
                'tiene_autoria': Firma.AutoriaDelFirmante.SeObtuvoAutoria
            }
        if Firma.Detalle:
            dev['detalle'] = self._extract_firma_detalle(Firma.Detalle)
        return dev

    def _extract_resumen(self, Resumen):
        dev = {
            'firmante': Resumen.Firmante,
            'identificacion': Resumen.Identificacion,
            'garantia_de_integridad_y_autenticidad': Resumen.GarantiaDeIntegridadYAutenticidad,
            'garantia_validez_en_el_tiempo': Resumen.GarantiaDeValidezEnElTiempo,
            'resultado': Resumen.ResultadoValidacion,
            'fecha_estampa_de_tiempo': Resumen.FechaEstampaDeTiempo,
            'tipo_identificacion': Resumen.TipoIdentificacion,
            'tiene_fecha_estampa_de_tiempo': Resumen.TieneFechaEstampaDeTiempo
        }

        return dev

    def _extract_resultado_resumen(self, Resumen):
        dev = {
            'garantia_de_integridad_y_autenticidad': Resumen.GarantiaDeIntegridadYAutenticidad,
            'garantia_validez_en_el_tiempo': Resumen.GarantiaDeValidezEnElTiempo,
            'resultado_de_validacion': Resumen.ResultadoValidacionDelDocumentoFirmado
        }
        if Resumen.ResumenDeFirmas:
            dev['resumen'] = [self._extract_resumen(firma) for firma in Resumen.ResumenDeFirmas.ResumenDeFirma]
        return dev

    def _extract_documento(self, result, ERRORES_VALIDACION):
        dev = {}
 #       dev.update(self.DEFAULT_DOCUMENT_ERROR(ERRORES_VALIDACION))
        dev['codigo_error'] = 0 if result.FueExitosa else 1
        dev['texto_codigo_error'] = get_text_representation(
            ERRORES_VALIDACION, dev['codigo_error']),
        dev['exitosa'] = result.FueExitosa
        dev['firmas'] = None
        dev['resumen'] = None
        dev['errores'] = None

        if result.ErrorGeneradoAlValidar:
            dev['errores'] = result.ErrorGeneradoAlValidar

        if result.Firmas:
            dev['firmas'] = [self._extract_firmas(firma) for firma in result.Firmas.Firma]

        if result.Resumen:
            dev['resumen'] = self._extract_resultado_resumen(result.Resumen)

        return dev

    def _validar_certificado_autenticacion(self, certificado):
        stub = ValidadorDeCertificadoSoapServiceStub()
        options = SoliciteLaValidacionDelCertificadoDeAutenticacion()
        options.elCertificadoDeAutenticacion = certificado
        status = stub.SoliciteLaValidacionDelCertificadoDeAutenticacion(
            options)
        result = status.soap_body.SoliciteLaValidacionDelCertificadoDeAutenticacionResult
        return self._extract_certificado_autenticacion(result)

    def _extract_certificado_autenticacion(self, result):
        dev = {
            'codigo_error': result.CodigoDeError,
            'texto_codigo_error': get_text_representation(
                ERRORES_VALIDA_CERTIFICADO, result.CodigoDeError),
            'exitosa': result.FueExitosa,
            'certificado': None

        }
        if result.FueExitosa:
            cert = result.InformacionDelCertificado
            dev['certificado'] = {
                'tipo_identificacion': cert.TipoDeIdentificacion,
                'identificacion': cert.Identificacion or 'N/D',
                'nombre': cert.NombreCompleto or 'N/D',
                'inicio_vigencia': cert.FechaInicioDeLaVigencia,
                'fin_vigencia': cert.FechaFinalDeLaVigencia}

        return dev

    def _validar_servicio_certificado(self):
        stub = ValidadorDeCertificadoSoapServiceStub()
        option = ValideServicioCertificado()
        try:
            status = stub.ValideElServicio(option)
            dev = status.soap_body.ValideElServicioResult
        except Exception as e:
            logger.error({'message': "Validador: Servicio de validado de certificado fallando",
                         'data': e, 'location': __file__})
            dev = False
        return dev

    def _validar_servicio_documento(self):
        stub = ValidadorDeDocumentosSoapServiceStub()
        option = ValideServicioDocumento()
        try:
            status = stub.ValideElServicio(option)
            dev = status.soap_body.ValideElServicioResult
        except Exception as e:
            logger.error({'message':
                "Validador: Servicio de validado de documentos fallando", 'data': e, 'location': __file__})
            dev = False

        return dev

'''
Created on 19 jul. 2017

@author: luis
'''

from pyfva.soap.validador_certificado import ValideElServicio as ValideServicioCertificado,\
    ValidadorDeCertificadoSoapServiceStub,\
    SoliciteLaValidacionDeCetificadoDeAutenticacion
from pyfva.soap.validador_documento import ValideElServicio as ValideServicioDocumento,\
    ValidadorDeDocumentoSoapServiceStub, ValideElDocumentoXmlEnvelopedCoFirma
from pyfva.soap import settings

import logging

logger = logging.getLogger('pyfva')


class ClienteValidador(object):
    """Permite validar una firma o un documento utilizando los servicios del BCCR

    .. note:: 
        Este servicio solo valida documento XML, por lo que no debe usarlo para odf o msoffice.
        Se espera que en un futuro pueda soportar los demás formatos.

    .. note:: 
        Los parámetros negocio y entidad de momento no son requeridos, pero puede que en un futuro cercano
        lo sean, por lo que se recomienda suministrarlos.

    :param negocio: número de identificación del negocio (provisto por el BCCR)
    :param entidad: número de identificación de la entidad (provisto por el BCCR)
    """
    DEFAULT_CERTIFICATE_ERROR = {
        'codigo_error': 2,
        'exitosa': False,
        'certificado': None

    }

    DEFAULT_DOCUMENT_ERROR = {
        'exitosa': False,
        'advertencias': None,
        'errores_encontrados': None,
        'firmantes': None,
    }

    def __init__(self,
                 negocio=settings.DEFAULT_BUSSINESS,
                 entidad=settings.DEFAULT_ENTITY):
        self.negocio = negocio
        self.entidad = entidad

    def validar_documento_xml(self, documento):
        """Valida si el documento está firmado correctamente.

        :param documento: documento xml en base64

        Retorna una diccionario con los siguientes elementos, en caso de error retorna
        **DEFAULT_DOCUMENT_ERROR**.

        .. note:: 
            Observe que en caso de no ser exitosa la operación los atributos 'advertencias', 'errores_encontrados' y 'firmantes' retornarán None

        :returns:   

            **exitosa:** True si fue exitoso el verificado del documento, False si no lo fue

            **advertencias:** Lista de advertencias encontradas durante el proceso de validadación, algo como: ["adv1", "adv2"]

            **errores_encontrados:** Lista de errores encontrados y su respectivo detalle, ej  
            [("código de error", "Detalle del error"), ...]

            **firmantes:** Lista de información del los firmantes, ej 
            [ {'identificacion': "8-0888-0888", 'fecha_firma': datetime.now(),
            'nombre': "Juanito Mora Porras"}, ... ]      
        """

        logger.debug("Validador: validar_documento_xml %r" % (locals(), ))
        try:
            dev = self._validar_documento_xml(documento)
        except Exception as e:
            logger.error("Validador: validando documento xml %s" % (e, ))
            dev = self.DEFAULT_DOCUMENTO_ERROR

        logger.debug("Validador: validar_documento_xml resultado %r" %
                     (dev, ))
        return dev

    def validar_certificado_autenticacion(self, certificado):
        """Valida si el certificado de autenticación es válido y no está revocado.

        :param certificado: Certificado en base64

        Retorna una diccionario con los siguientes elementos, en caso de error retorna
        **DEFAULT_CERTIFICATE_ERROR**.

        :returns:   
            **codigo_error:** Número con el código de error 1 es éxito

            **exitosa:** True si fue exitosa, False si no lo fue

            **certificado:** Si la operación no fue exitosa retorna None, si lo fue retorna un diccionario con:
                **identificacion:** Número de identificación del suscriptor dueño del certificado

                **nombre:**  Nombre completo del suscriptor dueño del certificado

                **inicio_vigencia:** Fecha de inicio del vigencia del certificado

                **fin_vigencia:** Fecha de finalización de la vigencia del certificado
        """

        logger.debug(
            "Validador: validar_certificado_autenticacion %r" % (locals(), ))
        try:
            dev = self._validar_certificado_autenticacion(certificado)
        except Exception as e:
            logger.error("Validador: validando certificado %s" % (e, ))
            dev = self.DEFAULT_CERTIFICATE_ERROR

        logger.debug(
            "Validador: validar_certificado_autenticacion result %r" % (dev, ))
        return dev

    def validar_servicio(self, servicio):
        """Valida si el servicio está disponible.  

        :param servicio: tipo de servicio a validar, puede ser 'certificado' o 'documento'
        :returns: True si lo está o False si ocurrió algún error contactando al BCCR o el servicio no está disponible
        """

        logger.info("Validador: Validar servicio %s" % (servicio, ))
        dev = False
        if servicio.lower() == 'certificado':
            dev = self._validar_servicio_certificado()
        elif servicio.lower() == 'documento':
            dev = self._validar_servicio_documento()

        logger.debug("Validador: Validar servicio %s %r" % (servicio, dev))
        return dev

    # Private methods
    def _validar_documento_xml(self, documento):
        stub = ValidadorDeDocumentoSoapServiceStub()
        options = ValideElDocumentoXmlEnvelopedCoFirma()
        options.elDocumentoXml = documento
        try:
            status = stub.ValideElDocumentoXmlEnvelopedCoFirma(options)
            dev = self._extract_documento_xml(
                status.soap_body.ValideElDocumentoXmlEnvelopedCoFirmaResult)
        except Exception as e:
            logger.error("Validador: validando  xml %s" % (e, ))
            dev = self.DEFAULT_DOCUMENT_ERROR

        return dev

    def _extract_documento_xml(self, result):
        if not result.FueExitosa:
            return self.DEFAULT_DOCUMENT_ERROR

        dev = {}
        dev.update(self.DEFAULT_DOCUMENT_ERROR)
        dev['exitosa'] = result.FueExitosa
        dev['advertencias'] = result.Advertencias.string
        dev['errores_encontrados'] = [(error.Codigo, error.Detalle)
                                      for error in result.ErroresEncontrados.ErrorDeDocumento]
        dev['firmantes'] = [
            {'identificacion': x.Cedula,
                'fecha_firma': x.FechaDeFirma,
                'nombre': x.NombreCompleto} for x in
            result.Firmantes.Firmante]

        return dev

    def _validar_certificado_autenticacion(self, certificado):
        stub = ValidadorDeCertificadoSoapServiceStub()
        options = SoliciteLaValidacionDeCetificadoDeAutenticacion()
        options.elCertificadoDeAutenticacion = certificado
        status = stub.SoliciteLaValidacionDeCetificadoDeAutenticacion(options)
        result = status.soap_body.SoliciteLaValidacionDeCetificadoDeAutenticacionResult
        return self._extract_certificado_autenticacion(result)

    def _extract_certificado_autenticacion(self, result):
        dev = {
            'codigo_error': result.CodigoDeError,
            'exitosa': result.FueExitosa,
            'certificado': None

        }
        if result.FueExitosa:
            cert = result.InformacionDelCertificado
            dev['certificado'] = {
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
            logger.error(
                "Validador: Servicio de validado de certificado fallando %s" % (e, ))
            dev = False
        return dev

    def _validar_servicio_documento(self):
        stub = ValidadorDeDocumentoSoapServiceStub()
        option = ValideServicioDocumento()
        try:
            status = stub.ValideElServicio(option)
            dev = status.soap_body.ValideElServicioResult
        except Exception as e:
            logger.error(
                "Validador: Servicio de validado de documentos fallando %s" % (e, ))
            dev = False

        return dev

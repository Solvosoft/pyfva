'''
Created on 19 jul. 2017

@author: luis
'''
import warnings
from pyfva.soap.validador_certificado import ValideElServicio as ValideServicioCertificado,\
    ValidadorDeCertificadoSoapServiceStub,\
    SoliciteLaValidacionDeCetificadoDeAutenticacion
from pyfva.soap.validador_documento import ValideElServicio as ValideServicioDocumento,\
    ValidadorDeDocumentoSoapServiceStub, ValideElDocumentoXmlEnvelopedCoFirma
from pyfva.soap import settings


class ClienteValidador(object):
    DEFAULT_CERTIFICATE_ERROR = {
        'cod_error': 2,
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
        try:
            dev = self._validar_documento_xml(documento)
        except:
            dev = self.DEFAULT_DOCUMENTO_ERROR

        return dev

    def validar_certificado_autenticacion(self, certificado):
        try:
            dev = self._validar_certificado_autenticacion(certificado)
        except:
            dev = self.DEFAULT_CERTIFICATE_ERROR

        return dev

    def validar_servicio(self, servicio):
        """ servicio puede ser 'certificado' o 'documento' """
        if servicio.lower() == 'certificado':
            return self._validar_servicio_certificado()
        if servicio.lower() == 'documento':
            return self._validar_servicio_documento()
        return False

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
            warnings.warn("Servicio de documento XML fallando %s" %
                          (e,), RuntimeWarning)
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
            'cod_error': result.CodigoDeError,
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
            warnings.warn("Servicio de validado de certificado fallando %s" %
                          (e,), RuntimeWarning)

            dev = False
        return dev

    def _validar_servicio_documento(self):
        stub = ValidadorDeDocumentoSoapServiceStub()
        option = ValideServicioDocumento()
        try:
            status = stub.ValideElServicio(option)
            dev = status.soap_body.ValideElServicioResult
        except Exception as e:
            warnings.warn("servicio de validado de documentos fallando %s" %
                          (e,), RuntimeWarning)

            dev = False
        return dev

'''
Created on 20 jul. 2017

@author: luis
'''
from pyfva.soap.verificador import ValideElServicio, VerificadorSoapServiceStub,\
    ExisteUnaSolicitudDeFirmaCompleta
import warnings


class ClienteVerificador(object):
    DEFAULT_ERROR = {
        'codigo_error': 2,
        'existe_firma': False,
        'fue_exitosa': False

    }

    def __init__(self, negocio=None, entidad=None):
        self.negocio = negocio
        self.entidad = entidad

    def existe_solicitud_de_firma_completa(self, identificacion):
        try:
            dev = self._existe_solicitud_de_firma_completa(identificacion)
        except:
            dev = self.DEFAULT_ERROR
        return dev

    def validar_servicio(self):
        return self._validar_servicio()

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
            warnings.warn("servicio de verificación fallando %s" %
                          (e,), RuntimeWarning)

            dev = False
        return dev

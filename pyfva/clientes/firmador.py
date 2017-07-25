'''
Created on 19 jul. 2017

@author: luis
'''
from pyfva.soap.firmador import FirmadorSoapServiceStub,\
    RecibaLaSolicitudDeFirmaXmlEnvelopedCoFirma, RecibaLaSolicitudDeFirmaODF,\
    RecibaLaSolicitudDeFirmaMSOffice, ValideElServicio,\
    ElSuscriptorEstaConectado, SolicitudDeFirma
import warnings
from pyfva.soap import settings

from datetime import datetime


class ClienteFirmador(object):
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
            warnings.warn("Formato de documento inválido", RuntimeWarning)
            dev = self.DEFAULT_ERROR
        return dev

    def construya_solicitud(self, identidad, documento, algoritmo_hash='Sha512', hash_doc=None, resumen=''):
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

    def firme_xml(self, identidad, documento, algoritmo_hash='Sha512', hash_doc=None, resumen=''):
        request = self.construya_solicitud(
            identidad, documento, algoritmo_hash, hash_doc, resumen)
        try:
            dev = self._firme_xml(request)
        except:
            dev = self.DEFAULT_ERROR
        return dev

    def firme_odf(self, identidad, documento, algoritmo_hash='Sha512', hash_doc=None, resumen=''):
        request = self.construya_solicitud(
            identidad, documento, algoritmo_hash, hash_doc, resumen)
        try:
            dev = self._firme_odf(request)
        except:
            dev = self.DEFAULT_ERROR
        return dev

    def firme_msoffice(self, identidad, documento, algoritmo_hash='Sha512', hash_doc=None, resumen=''):
        request = self.construya_solicitud(
            identidad, documento, algoritmo_hash, hash_doc, resumen)
        try:
            dev = self._firme_msoffice(request)
        except:
            dev = self.DEFAULT_ERROR
        return dev

    def suscriptor_conectado(self, identificacion):
        return self._suscriptor_conectado(identificacion)

    def validar_servicio(self):
        return self._validar_servicio()

    def extract_result(self, request,  result):
        try:
            data = self._extract_result(request,  result)
        except:
            data = self.DEFAULT_ERROR
        return data

    # Private methods
    def _extract_result(self, request, result):
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
        return self.extract_result(request,
                                   status.soap_body.RecibaLaSolicitudDeFirmaXmlEnvelopedCoFirmaResult)

    def _firme_odf(self, request):
        stub = FirmadorSoapServiceStub()
        options = RecibaLaSolicitudDeFirmaODF()
        options.laSolicitud = request
        status = stub.RecibaLaSolicitudDeFirmaODF(options)
        return self.extract_result(request,
                                   status.soap_body.RecibaLaSolicitudDeFirmaODFResult)

    def _firme_msoffice(self, request):
        stub = FirmadorSoapServiceStub()
        options = RecibaLaSolicitudDeFirmaMSOffice()
        options.laSolicitud = request
        status = stub.RecibaLaSolicitudDeFirmaMSOffice(options)
        return self.extract_result(request,
                                   status.soap_body.RecibaLaSolicitudDeFirmaMSOfficeResult)

    def _suscriptor_conectado(self, identificacion):
        stub = FirmadorSoapServiceStub()
        options = ElSuscriptorEstaConectado()
        options.laIdentificacion = identificacion
        try:
            status = stub.ElSuscriptorEstaConectado(options)
            dev = status.soap_body.ElSuscriptorEstaConectadoResult
        except Exception as e:
            warnings.warn("Servicio de firmado fallando en usuario conectado %s" %
                          (e,), RuntimeWarning)
            dev = False
        return dev

    def _validar_servicio(self):
        stub = FirmadorSoapServiceStub()
        option = ValideElServicio()
        try:
            status = stub.ValideElServicio(option)
            dev = status.soap_body.ValideElServicioResult
        except Exception as e:
            warnings.warn("servicio de firmado fallando %s" %
                          (e,), RuntimeWarning)

            dev = False
        return dev

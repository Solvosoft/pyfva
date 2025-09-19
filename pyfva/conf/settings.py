'''
Created on 11 de septiembre 2025

@author: luisza
'''
import logging
try:
    from collections.abc import Iterable
except:
    from collections import Iterable

DEFAULT_CONNECTION_TYPE="soap"
FVA_HOST = "http://bccr.fva.cr/"
LOGGING_PREFIX = ''
# FVA_HOST = 'http://bccr.fva.cr/'
STUB_SCHEME = 'http'
STUB_HOST = "localhost:8001"
#RECEPTOR_HOST = "http://localhost:8000/"
RECEPTOR_HOST = 'http://bccr.fva.cr/'

RECEPTOR_CLIENT = 'pyfva.receptor.client'

SELLADOR_CERT_PATH = ''
SELLADOR_KEY_PATH = ''

DEFAULT_BUSSINESS = 1
DEFAULT_ENTITY = 1

SERVICE_URLS = {
    'autenticacion': 'WebServices/Bccr.Firma.Fva.Entidades.Ws.BS/Autenticador.asmx',
    'firma': 'WebServices/Bccr.Firma.Fva.Entidades.Ws.BS/Firmador.asmx',
    'valida_certificado': 'WebServices/Bccr.Firma.Fva.Entidades.Ws.BS/ValidadorDeCertificado.asmx',
    'valida_documento': 'WebServices/Bccr.Firma.Fva.Entidades.Ws.BS/ValidadorDeDocumento.asmx',
    'valida_docs_v2': 'WebServices/Bccr.Firma.Fva.Entidades.ValidarDocumento.Ws.SI/ValidadorDeDocumentos.asmx',
    'verifica': 'WebServices/Bccr.Firma.Fva.Entidades.Ws.BS/Verificador.asmx',
    'sello': 'WebServices/Bccr.Firma.Fva.Entidades.Sello.Ws.SI/SelladorElectronicoConControlDeLlave.asmx'

}

TEST_SERVICE_URLS = {
    'autenticacion': 'WebServices/Bccr.Fva.Entidades.AmbienteDePruebas.Ws.BS/Autenticador.asmx',
    'firma': 'WebServices/Bccr.Fva.Entidades.AmbienteDePruebas.Ws.BS/Firmador.asmx',
    'valida_certificado': 'WebServices/Bccr.Firma.Fva.Entidades.Ws.BS/ValidadorDeCertificado.asmx',
    'valida_documento': 'WebServices/Bccr.Firma.Fva.Entidades.Ws.BS/ValidadorDeDocumento.asmx',
    'valida_docs_v2': 'WebServices/Bccr.Firma.Fva.Entidades.ValidarDocumento.Ws.SI/ValidadorDeDocumentos.asmx',
    'verifica': 'WebServices/Bccr.Fva.Entidades.AmbienteDePruebas.Ws.BS/Verificador.asmx',
    'sello': 'WebServices/Bccr.Fva.Entidades.AmbDePruebas.Sello.Ws.SI/SelladorElectronicoConControlDeLlave.asmx'
}

BASE_REST_URL='https://servicios-rest-firmador.gaudi.sinpe.fi.cr/FVA/'
REST_SERVICE_URLS={
    'autenticacion': 'Bccr.Firma.Fva.Entidades.Autenticar.API/Autenticar/RecibaLaSolicitudDeAutenticacion',
    'valida_autenticacion': 'Bccr.Firma.Fva.Entidades.Autenticar.API/Autenticar/ValideElServicio',
    'firma_suscriptor': 'Bccr.Firma.Fva.Entidades.FirmarDocumento.API/FirmadorDocumento/ElSuscriptorEstaConectado',
    'firma_msoffice': 'Bccr.Firma.Fva.Entidades.FirmarDocumento.API/FirmadorDocumento/RecibaLaSolicitudDeFirmaMSOffice',
    'firma_odf': 'Bccr.Firma.Fva.Entidades.FirmarDocumento.API/FirmadorDocumento/RecibaLaSolicitudDeFirmaODF',
    'firma_pdf': 'Bccr.Firma.Fva.Entidades.FirmarDocumento.API/FirmadorDocumento/RecibaLaSolicitudDeFirmaPdf',
    'firma_xml_cofirma': 'Bccr.Firma.Fva.Entidades.FirmarDocumento.API/FirmadorDocumento/RecibaLaSolicitudDeFirmaXmlEnvelopedCoFirma',
    'firma_xml_contafirma': 'Bccr.Firma.Fva.Entidades.FirmarDocumento.API/FirmadorDocumento/RecibaLaSolicitudDeFirmaXmlEnvelopedContraFirma',
    'valida_firma': 'Bccr.Firma.Fva.Entidades.FirmarDocumento.API/FirmadorDocumento/ValideElServicio'
}

TEST_REST_SERVICE_URLS = {
    'autenticacion': 'Bccr.Firma.Fva.AmbienteDePruebas.Entidades.Autenticar.API/Autenticar/RecibaLaSolicitudDeAutenticacion',
    'valida_autenticacion': 'Bccr.Firma.Fva.AmbienteDePruebas.Entidades.Autenticar.API/Autenticar/ValideElServicio',
    'firma_suscriptor': 'Bccr.Firma.Fva.AmbienteDePruebas.Entidades.FirmarDocumento.API/FirmadorDocumento/ElSuscriptorEstaConectado',
    'firma_msoffice': 'Bccr.Firma.Fva.AmbienteDePruebas.Entidades.FirmarDocumento.API/FirmadorDocumento/RecibaLaSolicitudDeFirmaMSOffice',
    'firma_odf': 'Bccr.Firma.Fva.AmbienteDePruebas.Entidades.FirmarDocumento.API/FirmadorDocumento/RecibaLaSolicitudDeFirmaODF',
    'firma_pdf': 'Bccr.Firma.Fva.AmbienteDePruebas.Entidades.FirmarDocumento.API/FirmadorDocumento/RecibaLaSolicitudDeFirmaPdf',
    'firma_xml_cofirma': 'Bccr.Firma.Fva.AmbienteDePruebas.Entidades.FirmarDocumento.API/FirmadorDocumento/RecibaLaSolicitudDeFirmaXmlEnvelopedCoFirma',
    'firma_xml_contafirma': 'Bccr.Firma.Fva.AmbienteDePruebas.Entidades.FirmarDocumento.API/FirmadorDocumento/RecibaLaSolicitudDeFirmaXmlEnvelopedContraFirma',
    'valida_firma': 'Bccr.Firma.Fva.AmbienteDePruebas.Entidades.FirmarDocumento.API/FirmadorDocumento/ValideElServicio'
}

WS_URL_NOTIFICATION = 'wcfv2/Bccr.Sinpe.Fva.EntidadDePruebas.Notificador/ResultadoDeSolicitud.asmx'
PYFVA_TIMEZONE = 'America/Costa_Rica'

import sys
import os

logger = logging.getLogger('pyfva')
def load_settings(settings):
    thismodule = sys.modules[__name__]
    for name in ['FVA_HOST',
                 'STUB_SCHEME',
                 'STUB_HOST',
                 'RECEPTOR_HOST',
                 'DEFAULT_BUSSINESS',
                 'DEFAULT_ENTITY',
                 'RECEPTOR_CLIENT',
                 'SELLADOR_CERT_PATH',
                 'SELLADOR_KEY_PATH',
                 'WS_URL_NOTIFICATION',
                 'PYFVA_TIMEZONE',
                 'LOGGING_PREFIX',
                 'DEFAULT_CONNECTION_TYPE',
                 'BASE_REST_URL']:


        if hasattr(settings, name):
            setattr(thismodule, name,
                    getattr(settings, name)
                    )
        elif isinstance(settings, os._Environ) and name in settings:
            setattr(thismodule, name,
                    settings[name]
                    )
    if DEFAULT_CONNECTION_TYPE == 'soap':
        if hasattr(settings, "FVA_TESTURLS") or ( isinstance(settings, os._Environ) and "FVA_TESTURLS" in settings):
            setattr(thismodule, 'SERVICE_URLS', TEST_SERVICE_URLS)
    else:
        if hasattr(settings, "FVA_TESTURLS") or ( isinstance(settings, os._Environ) and "FVA_TESTURLS" in settings):
            setattr(thismodule, 'SERVICE_URLS', TEST_REST_SERVICE_URLS)
        else:
            setattr(thismodule, 'SERVICE_URLS', REST_SERVICE_URLS)
try:
    from django.conf import settings as djsettings
    load_settings(djsettings)
except Exception as e:
    logger.debug(e)
    logger.info("No django configuration detected, using environment")

load_settings(os.environ)

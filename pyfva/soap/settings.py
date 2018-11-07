'''
Created on 24 jul. 2017

@author: luis
'''


FVA_HOST = "http://bccr.fva.cr/"
# FVA_HOST = 'http://bccr.fva.cr/'
STUB_SCHEME = 'http'
STUB_HOST = "localhost:8001"
#RECEPTOR_HOST = "http://localhost:8000/"
RECEPTOR_HOST = 'http://bccr.fva.cr/'

RECEPTOR_CLIENT = 'pyfva.receptor.client'

DEFAULT_BUSSINESS = 1
DEFAULT_ENTITY = 1

SERVICE_URLS = {
    'autenticacion': 'WebServices/Bccr.Firma.Fva.Entidades.Ws.BS/Autenticador.asmx',
    'firma': 'WebServices/Bccr.Firma.Fva.Entidades.Ws.BS/Firmador.asmx',
    'valida_certificado': 'WebServices/Bccr.Firma.Fva.Entidades.Ws.BS/ValidadorDeCertificado.asmx',
    'valida_documento': 'WebServices/Bccr.Firma.Fva.Entidades.Ws.BS/ValidadorDeDocumento.asmx',
    'verifica': 'WebServices/Bccr.Firma.Fva.Entidades.Ws.BS/Verificador.asmx'
}

SERVICE_URLS = {
    'autenticacion': 'WebServices/Bccr.Firma.Fva.Entidades.Ws.BS/Autenticador.asmx',
    'firma': 'WebServices/Bccr.Firma.Fva.Entidades.Ws.BS/Firmador.asmx',
    'valida_certificado': 'WebServices/Bccr.Firma.Fva.Entidades.Ws.BS/ValidadorDeCertificado.asmx',
    'valida_documento': 'WebServices/Bccr.Firma.Fva.Entidades.Ws.BS/ValidadorDeDocumento.asmx',
    'verifica': 'WebServices/Bccr.Firma.Fva.Entidades.Ws.BS/Verificador.asmx'
}

TEST_SERVICE_URLS = {
    'autenticacion': 'WebServices/Bccr.Fva.Entidades.AmbienteDePruebas.Ws.BS/Autenticador.asmx',
    'firma': 'WebServices/Bccr.Fva.Entidades.AmbienteDePruebas.Ws.BS/Firmador.asmx',
    'valida_certificado': 'WebServices/Bccr.Firma.Fva.Entidades.Ws.BS/ValidadorDeCertificado.asmx',
    'valida_documento': 'WebServices/Bccr.Firma.Fva.Entidades.Ws.BS/ValidadorDeDocumento.asmx',
    'verifica': 'WebServices/Bccr.Fva.Entidades.AmbienteDePruebas.Ws.BS/Verificador.asmx'
}

WS_URL_NOTIFICATION = 'wcfv2/Bccr.Sinpe.Fva.EntidadDePruebas.Notificador/ResultadoDeSolicitud.asmx'

import sys
import os


def load_settings(settings):
    thismodule = sys.modules[__name__]

    for name in ['FVA_HOST',
                 'STUB_SCHEME',
                 'STUB_HOST',
                 'RECEPTOR_HOST',
                 'DEFAULT_BUSSINESS',
                 'DEFAULT_ENTITY',
                 'RECEPTOR_CLIENT',
                 'WS_URL_NOTIFICATION']:

        if hasattr(settings, name):
            setattr(thismodule, name,
                    getattr(settings, name)
                    )
        elif name in settings:
            setattr(thismodule, name,
                    settings[name]
                    )

    if hasattr(settings, "FVA_TESTURLS") or "FVA_TESTURLS" in settings:
        setattr(thismodule, 'SERVICE_URLS', TEST_SERVICE_URLS)


try:
    from django.conf import settings as djsettings
    load_settings(djsettings)
except:
    pass

load_settings(os.environ)

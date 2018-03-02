from pyfva.clientes.autenticador import ClienteAutenticador
from pyfva.clientes.firmador import ClienteFirmador
from pyfva.clientes.validador import ClienteValidador
from pyfva.clientes.verificador import ClienteVerificador

import warnings
import logging
logging.basicConfig(filename='pyfva.log',level=logging.DEBUG)

## ---------------------AUTENTICACIÓN ------------------------------##

authclient = ClienteAutenticador(1,1) # negocio, entidad

if authclient.validar_servicio():
    data = authclient.solicitar_autenticacion('08-0888-0888', -1)
    print(data)
else:
    warnings.warn("Autenticación BCCR No disponible", RuntimeWarning)
    data = authclient.DEFAULT_ERROR


## ---------------------FIRMA ------------------------------##

signclient = ClienteFirmador(negocio=1, entidad=1)
if signclient.validar_servicio():
    for formato in ['xml_cofirma', 'xml_contrafirma', 'odf', 'msoffice', 'pdf']:
        data = signclient.firme(
        '08-0888-0888',
        """PG1vdmllPgogIDx0...CjwvbW92aWU+Cg==""",
        formato,  # xml, odf, msoffice
        algoritmo_hash='Sha512',  # Sha256, Sha384, Sha512
        hash_doc="""637a7d07c5dbee59695aafbd3933b...bd3933b""",
        resumen="este es un mensaje amigable sobre el documento", 
        id_funcionalidad=-1)
        print(formato,"\t-->\t", data)
else:
    warnings.warn("Firmador BCCR No disponible", RuntimeWarning)
    data = signclient.DEFAULT_ERROR

## ---------------------VALIDACIÓN ------------------------------##

clientvalida = ClienteValidador()
if clientvalida.validar_servicio('certificado'):  
    data = clientvalida.validar_certificado_autenticacion(
        """PG1vdmllPgogIDx...2aWU+Cg==""")
    print(data)
else:
    warnings.warn(
        "Validar certificado BCCR No disponible", RuntimeWarning)
    data = clientvalida.DEFAULT_CERTIFICATE_ERROR

if clientvalida.validar_servicio('documento'):
    for formato in ['cofirma', 'contrafirma', 'msoffice', 'odf', 'pdf']:
        data = clientvalida.validar_documento("""DG2vdmllPgogIDx...2bWU++g==""", formato)
        print(formato, "\t-->\t", data)
else:
    warnings.warn(
        "Validar documento BCCR No disponible", RuntimeWarning)
    data = clientvalida.DEFAULT_DOCUMENT_ERROR

## ---------------------VERIFICACIÓN ------------------------------##

clientverifica = ClienteVerificador()
if clientverifica.validar_servicio():
    data = clientverifica.existe_solicitud_de_firma_completa('08-0888-0888')
else:
    warnings.warn(
    "Verificar firma completa BCCR No disponible",
    RuntimeWarning)
    data = clientverifica.DEFAULT_ERROR

import logging
import warnings

from pyfva.clientes.validadorv2 import ClienteValidador

logging.basicConfig(filename='pyfva.log',level=logging.DEBUG)


## ---------------------VALIDACIÓN ------------------------------##

clientvalida = ClienteValidador()
#if clientvalida.validar_servicio('certificado'):
#    data = clientvalida.validar_certificado_autenticacion(
#        """PG1vdmllPgogIDx...2aWU+Cg==""")
#    print(data)
#else:
#    warnings.warn(
#        "Validar certificado BCCR No disponible", RuntimeWarning)
#    data = clientvalida.DEFAULT_CERTIFICATE_ERROR

#if clientvalida.validar_servicio('documento'):
for formato in  ['cofirma', 'contrafirma', 'msoffice', 'odf', 'pdf']:

    data = clientvalida.validar_documento("""DG2vdmllPgogIDx...2bWU++g==""", formato)
    print(formato, "\t-->\t", data)
#else:
#    warnings.warn(
#        "Validar documento BCCR No disponible", RuntimeWarning)
#    data = clientvalida.DEFAULT_DOCUMENT_ERROR


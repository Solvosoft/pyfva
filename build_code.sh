#!/bin/sh


mkdir -p tmp

# Autenticador
python -m soapfish.wsdl2py -c WSDL/Autenticador.xml > tmp/authenticator.py
meld pyfva/soap/autenticador.py tmp/authenticator.py

# Firmador
python -m soapfish.wsdl2py -c WSDL/Firmador.xml > tmp/firmador.py
meld pyfva/soap/firmador.py tmp/firmador.py


# Verificador 
python -m soapfish.wsdl2py -c WSDL/Verificador.xml > tmp/verificador.py
meld pyfva/soap/verificador.py tmp/verificador.py

# Validador Certificados
python -m soapfish.wsdl2py -c WSDL/ValidadorDeCertificado.xml > tmp/validadordecertificado.py
meld pyfva/soap/validador_certificado.py  tmp/validadordecertificado.py

# Validador de Documentos

python -m soapfish.wsdl2py -c WSDL/ValidadorDeDocumento.xml > tmp/validadordedocumento.py
meld pyfva/soap/validador_documento.py tmp/validadordedocumento.py

python -m soapfish.wsdl2py -c WSDL/ValidadorDeDocumentos_WS.wsdl > tmp/validador_documento_v2.py
meld pyfva/soap/validador_documento_v2.py tmp/validador_documento_v2.py

# Cliente receptor en las aplicaciones
python -m soapfish.wsdl2py -c WSDL/Receptor.xml > tmp/receptor.py
meld pyfva/receptor/ws_service.py tmp/receptor.py



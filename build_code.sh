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


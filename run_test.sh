#!/bin/bash

CERTSDIR=`pwd`/certs
export DEFAULT_CONNECTION_TYPE='soap' # soap rest
export DEBUG_HTTP_SERVER=0    #para utilizar fva_simulador

# --- Opciones de depuración ---
# LOG_LEVEL    nivel de log de pyfva, pyfva_exception y soapfish: DEBUG, INFO,
#              WARNING o ERROR (por defecto ERROR = salida mínima, solo errores)
#              usa DEBUG para ver el XML de la petición/respuesta SOAP completo
# HTTP_DEBUG=1 muestra el volcado crudo del socket HTTP (cabeceras y cuerpo tal
#              como viajan por la red, incluyendo la respuesta de error del servidor)
# VERBOSITY    nivel de detalle de unittest: 0 (silencioso), 1 (normal) o 2 (detallado)
export LOG_LEVEL=${LOG_LEVEL:-ERROR}
export HTTP_DEBUG=${HTTP_DEBUG:-0}
export VERBOSITY=${VERBOSITY:-2}

if [ $DEBUG_HTTP_SERVER -eq 0 ]; then
  export REQUESTS_CA_BUNDLE=$CERTSDIR/ca_nacional_de_CR.pem
  export REQUESTS_CA_PATH=$CERTSDIR/ca_nacional_de_CR.pem
  export REQUESTS_CERT_PATH=$CERTSDIR/bccr_agent.pem
  export REQUESTS_KEY_PATH=$CERTSDIR/bccr_agent_key.pem
  export STUB_SCHEME='https'
  export STUB_HOST="firmadorexterno.bccr.fi.cr"

  export DEFAULT_BUSSINESS=1
  export DEFAULT_ENTITY=1
  export FVA_TESTURLS=True
fi

run_tests() {
  python -c "
import logging, os, sys, unittest

level = getattr(logging, os.environ.get('LOG_LEVEL', 'ERROR').upper(), logging.ERROR)
logging.basicConfig(
    level=level,
    format='%(asctime)s %(levelname)s %(name)s: %(message)s',
)
for name in ('pyfva', 'pyfva_exception', 'soapfish', 'requests', 'urllib3'):
    logging.getLogger(name).setLevel(level)

if os.environ.get('HTTP_DEBUG') == '1':
    import http.client
    http.client.HTTPConnection.debuglevel = 1

sys.argv = ['unittest'] + sys.argv[1:]
unittest.main(module=None, verbosity=int(os.environ.get('VERBOSITY', 2)))
" "$@"
}

run_tests pyfva.tests
#run_tests pyfva.tests.soap.firmador.TestFirmador.test_sign_vacio
#run_tests pyfva.tests.soap.firmador.TestFirmador.test_valide_servicio
#run_tests pyfva.tests.rest.autenticador.TestAuthenticador.test_auth_nonotificado

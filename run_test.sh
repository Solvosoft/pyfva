#!/bin/bash

CERTSDIR=`pwd`/certs

export DEBUG_HTTP_SERVER=0    #para utilizar fva_simulador

if [ $DEBUG_HTTP_SERVER -eq 0 ]; then
  export REQUESTS_CA_BUNDLE=$CERTSDIR/ca_nacional_de_CR.pem
  export REQUESTS_CA_PATH=$CERTSDIR/ca_nacional_de_CR.pem
  export REQUESTS_CERT_PATH=$CERTSDIR/bccr_agent.pem
  export REQUESTS_KEY_PATH=$CERTSDIR/bccr_agent_key.pem
  export STUB_SCHEME='https'
  export STUB_HOST="firmadorexterno.bccr.fi.cr"
  export FVA_TESTURLS="True"

  export DEFAULT_BUSSINESS=1
  export DEFAULT_ENTITY=1
  export FVA_TESTURLS=True
fi

python -m unittest pyfva.tests

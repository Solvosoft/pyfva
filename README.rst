pyfva
#######

Cliente para conectar instituciones con BCCR_ FVA.

Abstrae la comunicación entre los servicios SOAP del BCCR_  y python creando clientes de fácil uso, por ejemplo si se desea autenticar a una persona se realizaría como

.. code:: python

    from pyfva.clientes.autenticador import ClienteAutenticador

    authclient = ClienteAutenticador(1,1) # negocio, entidad
                                             
    if authclient.validar_servicio():
        data = authclient.solicitar_autenticacion('08-0888-0888')
    else:
        # warnings.warn("Auth BCCR No disponible", RuntimeWarning)
        data = authclient.DEFAULT_ERROR

.. _BCCR: http://www.bccr.fi.cr/

Instalación
##############

.. note:: 
    Solo ha sido probado en python 3.

Instale mediante pypi

.. code:: bash

    pip install pyfva

o usando el repositorio 

.. code:: bash

    pip install git+https://github.com/solvo/pyfva.git

Documentación
################

Por supuesto la documentoación está aquí_

.. _aquí: http://pyfva.readthedocs.io/

Parámetros de ambiente
#############################

Los siguientes parámetros pueden ser modificados usando variables de entorno o variables en django settings.

Los valores por defecto son: 

* FVA_HOST = "http://bccr.fva.cr/"
* RECEPTOR_HOST = 'http://bccr.fva.cr/'

Ambos son direcciones del esquema, deben ser iguales al esquema del servicio WSDL.

* STUB_SCHEME = 'http'
* STUB_HOST = "localhost:8001"

Dirección y protocolo donde se ubica el servicio FVA.

* DEFAULT_BUSSINESS = 1
* DEFAULT_ENTITY = 1

Números de identificación en el servicio FVA. (en el simulador no son usados).

* RECEPTOR_CLIENT = 'pyfva.receptor.client'

Cliente para recibir las respuestas del FVA.

Configurando entorno del BCCR externo
#######################################
Las siguientes configuraciones son requeridas, los archivos deben estar en formato PEM

* REQUESTS_CA_BUNDLE=/<ruta de archivo>/ca_nacional_de_CR.pem
* REQUESTS_CA_PATH=/<ruta de archivo>/ca_nacional_de_CR.pem
* REQUESTS_CERT_PATH=/<ruta de archivo>/bccr_agent.pem
* REQUESTS_KEY_PATH=/<ruta de archivo>/bccr_agent_key.pem
* STUB_SCHEME = 'https'
* STUB_HOST = "firmadorexterno.bccr.fi.cr"


Generar documentoación
#############################

Instale Sphinx mediante pypi

.. code:: bash

    pip install -U Sphinx sphinx_rtd_theme

Cambiese de directorio y ejecute la creación de códigos

.. code:: bash

    cd docs
    bash build_doc.sh

Para regenerar la documentación, si no se tienen cambios en los códigos de error

.. code:: bash

    make html



Instalación y Configuración
===============================


Instalación
-------------------

.. note::
    Solo ha sido probado en python 3 en Debian 13 y con python3.13 .

Instale mediante pypi

.. code:: bash

    pip install pyfva

o usando el repositorio

.. code:: bash

    pip install -e "git+https://github.com/solvo/pyfva.git#egg=pyfva"


Instalación Windows
------------------------

Pyfva se desarrolla y prueba en Linux por lo que se recomienda encarecidamente usarlo, aún así debería ser compatible con Windows.

Los siguientes pasos corresponden a como lograrlo instalar

* Instale python 3 desde https://www.python.org/downloads/, (versión usada 3.13)
* Instale git  descargandolo desde https://git-scm.com/download/win

Es recomendable usar la terminal provista por git

* pip install pyfva


Parámetros de ambiente
--------------------------

Los siguientes parámetros pueden ser modificados usando variables de entorno o variables en django settings.

Los valores por defecto son:

* FVA_HOST = "http://bccr.fva.cr/"
* STUB_SCHEME = 'http'
* STUB_HOST = "localhost:8001"
* RECEPTOR_HOST = 'http://bccr.fva.cr/'
* DEFAULT_BUSSINESS = 1
* DEFAULT_ENTITY = 1
* RECEPTOR_CLIENT = 'pyfva.receptor.client'
* FVA_TESTURLS = ''

Para usar el cliente de Rest usando api json se deben asignar las siguientes variables

* RECEPTOR_CLIENT = 'pyfva.receptor.rest'
* DEFAULT_CONNECTION_TYPE = 'rest'

Para usarse en una consola en linux use por ejemplo:

.. code:: bash

    export STUB_HOST="localhost:8000"

y luego ejecute el programa que hace uso de pyfva.

En el caso de utilizar el entorno de pruebas se requiere especificar true, la no existencia de la variable representa,
el uso de las URL para producción.

.. code:: bash

    export FVA_TESTURLS="true"

.. note::
    No usar FVA_TESTURLS="true" cuando se use con el simulador, ya que este de momento no soporta las rutas de prueba.

En caso de usarse en conjunto con django puede agregar los parámetros en settings.py y serán cargados automáticamente.

.. note::
    Las variables de entorno tiene prioridad con respecto a las variables en settings de django


Comunicación SSL
--------------------------

Para entablar comunicación entre la entidad y el BCCR se requiere autenticación mutua, para esto debe indicar a nivel de entorno que las rutas de los certificados a utilizar.

.. code:: bash

    export REQUESTS_CA_PATH=ca_nacional_de_CR.pem
    export REQUESTS_CERT_PATH=bccr_agent.pem
    export REQUESTS_KEY_PATH=bccr_agent_key.pem

Por limitaciones de `requests` la llave privada debe estar en plano, por lo que se recomienda proteger especialmente ese archivo contra accesos indebidos.


Instalación y Configuración
===============================


Instalación
-------------------

.. note:: 
    Solo ha sido probado en python 3.

Instale mediante pypi

.. code:: bash

    pip install pyfva

o usando el repositorio 

.. code:: bash

    pip install git+https://github.com/solvo/crdist.git


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

Para usarse en una consola en linux use por ejemplo:

.. code:: bash

    export STUB_HOST="localhost:8000"

y luego ejecute el programa que hace uso de pyfva.

En caso de usarse en conjunto con django puede agregar los parámetros en settings.py y serán cargados automáticamente.

.. note:: 
    Las variables de entorno tiene prioridad con respecto a las variables en settings de django

pyfva
#######

Cliente para conectar instituciones con BCCR FVA.

Instalación
##############

.. code::bash

    pip install pyfva


Parámetros de ambiente
#############################

Los siguientes parámetros pueden ser modificados usando variables de entorno o variables en django settings.

Los valores por defecto son: 

* FVA_HOST = "http://bccr.fva.cr/"
* STUB_SCHEME = 'http'
* STUB_HOST = "localhost:8001"
* RECEPTOR_HOST = 'http://bccr.fva.cr/'
* DEFAULT_BUSSINESS = 1
* DEFAULT_ENTITY = 1

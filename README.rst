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

    pip install git+https://github.com/solvo/crdist.git

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
* RECEPTOR_CLIENT = 'pyfva.receptor.client'

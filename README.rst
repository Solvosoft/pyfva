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

Enlaces de interés
#######################

Los siguientes enlaces son de proyectos de interés relacionados con el desarrollo de firma digital.

- `Receptor de Notificiaciones BCCR`_
- `Ventanas de Usuario`_
- `Pyfva: Cliente para integración con Python`_
- `Firmador Libre, aplicación de escritorio`_


.. _`Receptor de Notificiaciones BCCR`: https://git.ucr.ac.cr/firma_comunidad/receptor-de-notificaciones-del-bccr
.. _`Ventanas de Usuario`: https://git.ucr.ac.cr/firma_comunidad/ventanas_usuario
.. _`Pyfva: Cliente para integración con Python`: https://github.com/solvo/pyfva
.. _`Firmador Libre, aplicación de escritorio`: https://gitlab.com/firmador/firmador

Instalación
##############


Instale mediante pypi

.. code:: bash

    pip install pyfva[soap]

o usando el repositorio

.. code:: bash

    pip install git+https://github.com/solvo/pyfva.git

en caso de solo querer los servicios Rest

   pip install pyfva

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

.. note:: En la mayoría de los casos el DEFAULT_ENTITY será 1 y el DEFAULT_BUSSINESS corresponde al

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


Para realizar pruebas de conexión es importante configurar una comunicación por ssl, los siguientes comándos pueden ser de ayuda

1. Unifica la cadena de certificados de confianza

Puede descargarse desde

- https://www.bccr.fi.cr/firma-digital/DocFirmaDigital/Jerarquia-Persona-Juridica-Produccion-entregar-entidades-externas.zip

Convierta los archivos a PEM

.. code:: bash

    openssl x509 -in 'CA POLITICA PERSONA JURIDICA - COSTA RICA v2.cer' -out 'CA POLITICA PERSONA JURIDICA - COSTA RICA v2.pem' -inform DER
    openssl x509 -in 'CA SINPE - PERSONA JURIDICA v2.cer' -out 'CA SINPE - PERSONA JURIDICA v2.pem' -inform DER
    openssl x509 -in 'CA RAIZ NACIONAL - COSTA RICA v2.cer' -out 'CA RAIZ NACIONAL - COSTA RICA v2.pem' -inform DER
    cp 'Certificado BANCO CENTRAL DE COSTA RICA (AGENTE ELECTRONICO).cer' 'Certificado BANCO CENTRAL DE COSTA RICA (AGENTE ELECTRONICO).pem'
    cp 'CA SINPE - PERSONA JURIDICA v2(1).crt' 'CA SINPE - PERSONA JURIDICA v2(1).pem'

.. code:: bash

    cat  'CA RAIZ NACIONAL - COSTA RICA v2.pem' 'CA POLITICA PERSONA JURIDICA - COSTA RICA v2.pem' 'CA SINPE - PERSONA JURIDICA v2.pem' 'CA SINPE - PERSONA JURIDICA v2(1).pem' > ca_nacional_de_CR.pem

2. Verifique que su certificado está validado por la CA que acaba de crear

.. code:: bash

    openssl verify -verbose -CAfile ca_nacional_de_CR.pem  bccr_agent.pem

3. Verifica que puede realizar una conexión con el BCCR autenticándose con el certificado

.. code:: bash

    curl --http1.1 --cert bccr_agent.pem --key bccr_agent_key.pem --cacert ca_nacional_de_CR.pem https://firmadorexterno.bccr.fi.cr:443/WebServices/Bccr.Fva.Entidades.AmbDePruebas.Sello.Ws.SI/SelladorElectronicoConControlDeLlave.asmx?wsdl

4. Verifique que puede puede recibir notificaciones

.. code:: bash

   openssl s_server -key bccr_agent_key.pem -cert bccr_agent.pem -CAfile ca_nacional_de_CR.pem -accept 8443 -www -tlsextdebug -debug -cipher ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES128-SHA:AES128-SHA256:AES256-SHA256 -tls1_2 -named_curve P-256

Las siguientes funciones pueden ser de ayuda para deteminar los cálculos

.. code:: python

    def get_digest(digest_name):
        if 'sha256' == digest_name:
            return hashlib.sha256()
        elif 'sha384' == digest_name:
            return hashlib.sha384()
        elif 'sha512' == digest_name:
            return hashlib.sha512()
    def get_hash_sum(data, algorithm, b64=False):
        if type(data) == str:
            data = data.encode()
        digest = get_digest(algorithm)
        digest.update(data)
        if b64:
            return base64.b64encode(digest.digest()).decode()
        hashsum = digest.hexdigest()
        return hashsum

Para leer un archivo se puede utilizar algo como esto

.. code:: python

    with open('/<ruta al archivo>/test.docx', 'rb') as arch:
        FI = arch.read()
        ARCH = base64.b64encode(FI).decode()
        HASH = get_hash_sum(FI, 'sha512', b64=True)
        data = stampclient.firme(ARCH, 'msoffice', hash_doc=HASH)

Generar documentación
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



Correr las pruebas
#############################

Cree una carpeta llamada  **certs** en la base del proyecto y ponga ahí los certificados y llaves privadas

* ca_nacional_de_CR.pem
* bccr_agent.pem
* bccr_agent_key.pem

Se necesita correr la aplicación que recibirá las peticiones desde el BCCR


.. code:: bash

    cd demo
    ./run_receptor.sh

En caso de correrse de forma local no olvidar

.. code:: bash

    python manage.py createcachetable

Luego sobre pyfva se ejecuta

.. code:: bash

    python -m unittest pyfva.tests


Crear y correr con Docker las pruebas
#######################################

note:: El archivo run_test.sh debe modificar el negocio y la entidad antes de generar la imagen

El receptor escucha el puerto 0.0.0.0:8443/notifica, esto debería estar registrado en central directo con el nombre de dominio
adecuado.

Para construir la imagen.

.. code:: bash

    docker build -t pyfva .



Para correr una instancia de pruebas.

.. code:: bash

    docker run --name pyfvatest -v  `pwd`/certs:/app/certs -p 8443:8443 pyfva

Para correr las pruebas.

.. code:: bash

    docker exec -ti  pyfvatest bash
    cd /app
    bash run_test.sh

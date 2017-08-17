Tutorial
===========

Este tutorial muestra cómo utilizar los clientes de FVA, sin entrar en detalles de muchos de los parámetros existentes, para saber con mayor detalle el funcionamiento del programa revisa :ref:`doc_clientes`.

.. note:: 
    Recuerde la política del banco es *no nos llame, nosotros lo llamamos*, por lo que muchos de los resultados obtenidos son estados de la transacción y no corresponden al resultado del proceso completo.

Autenticación
--------------------

Para solicitar a un suscriptor autenticación se debe usar el cliente ClienteAutenticador, por ejemplo

.. code:: python

    from pyfva.clientes.autenticador import ClienteAutenticador
    import warnings

    authclient = ClienteAutenticador(1,1) # negocio, entidad
                                             
    if authclient.validar_servicio():
        data = authclient.solicitar_autenticacion('08-0888-0888')
    else:
        warnings.warn("Autenticación BCCR No disponible", RuntimeWarning)
        data = authclient.DEFAULT_ERROR

El formato de la identificación debe respetar los formatos de codificación del BCCR para :ref:`formato_identificacion`.

Firma
------------

De momento se puede firmar documentos en los formatos XML, Open Document Format (ODF) y Microsoft Office.  Para ello debe utilizar el ClienteFirmador, por ejemplo:

.. code:: python 

    from pyfva.clientes.firmador import ClienteFirmador
    import warnings

    signclient = ClienteFirmador(
        negocio=1,
        entidad=1,
    )
    if signclient.validar_servicio():
        data = signclient.firme(
            '08-0888-0888',
            """PG1vdmllPgogIDx0...CjwvbW92aWU+Cg==""",
            "xml",  # xml, odf, msoffice
            algoritmo_hash='Sha512',  # Sha256, Sha384, Sha512
            hash_doc="""637a7d07c5dbee59695aafbd3933b...bd3933b""",
            resumen="este es un mensaje amigable sobre el documento")

    else:
        warnings.warn("Firmador BCCR No disponible", RuntimeWarning)
        data = signclient.DEFAULT_ERROR

El formato de la identificación debe respetar los formatos de codificación del BCCR para :ref:`formato_identificacion`.

Validación
---------------

Para validar los certificados de autenticación y los documentos firmados debe utilizar el ClienteValidador de la siguiente forma:

Al Validar un certificado use lo siguiente:

.. code:: python 

    from pyfva.clientes.validador import ClienteValidador
    import warnings

    client = ClienteValidador()
    if client.validar_servicio('certificado'):  
        data = client.validar_certificado_autenticacion(
            """PG1vdmllPgogIDx...2aWU+Cg==""")
    else:
        warnings.warn(
            "Validar certificado BCCR No disponible", RuntimeWarning)
        data = client.DEFAULT_CERTIFICATE_ERROR

Al validar un **documento XML** use lo siguiente:

.. code:: python 

    from pyfva.clientes.validador import ClienteValidador
    import warnings

    client = ClienteValidador()
    if client.validar_servicio('documento'):

        data = client.validar_documento_xml(
            """DG2vdmllPgogIDx...2bWU++g==""")

    else:
        warnings.warn(
            "Validar documento BCCR No disponible", RuntimeWarning)
        data = client.DEFAULT_DOCUMENT_ERROR

.. note:: 
    Documentos ODF y Microsoft office no están soportados todavía.

Verificación
--------------

La política "No nos llame, nosotros lo llamamos", genera que cuando se hace una firma o una autenticación exista un lapso de tiempo (mientras el usuario firma) en el que la aplicación no sabe si la operación de firma se hizo correctamente o no, para saber durante ese lapso si el usuario está firmando o ya completó su firma se usa el ClienteVerificador, por ejemplo

.. code:: python 

    from pyfva.clientes.verificador import ClienteVerificador
    import warnings

    client = ClienteVerificador()
    if client.validar_servicio():
        data = client.existe_solicitud_de_firma_completa('08-0888-0888')
    else:
        warnings.warn(
        "Verificar firma completa BCCR No disponible", 
        RuntimeWarning)
        data = client.DEFAULT_ERROR
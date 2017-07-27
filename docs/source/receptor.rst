Servicio receptor de respuestas del BCCR
====================================================

Bajo la política *No nos llame, nosotros lo llamamos* se requiere un cliente capaz de recibir las notificaciones del FVA del banco central,
por ello se ha previsto un cliente capaz de comunicarse.

.. note:: 
    Por defecto este módulo solo registra los eventos en debug, por lo que no aporta lógica, ni maneja 
    la petición, para ello mejor cree un cliente propio y modifique la variable de entorno *RECEPTOR_CLIENT*

Para construir un cliente que porporcione mayor funcionalidad solo debe hacer un módulo que posea los siguientes métodos:

* reciba_notificacion(data)
* valide_servicio()

Use el cliente de debug para saber cuales son los datos suministrados.

Cliente receptor para debug
------------------------------


.. automodule:: pyfva.receptor.client
    :members:
    :undoc-members:
    :member-order: bysource

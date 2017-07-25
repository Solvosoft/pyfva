Formátos y códigos
=====================

Acá se describe los formatos y los códigos utilizados por el BCCR en sus comunicaciones, los cuales además son usados por pyfva

Formato de identificación
------------------------------

El formato está basado en el documento `Codificaciones generales del sistema de pagos`_


.. _Codificaciones generales del sistema de pagos: http://www.bccr.fi.cr/sistema_pagos/servicios_sinpe/nuevos_servicios/NormaCodificaciones.pdf


.. _formato_identificacion:

Persona Física Nacional (Cédula de Identidad)
################################################

El estándar definido por la Registro Nacional para el número de identificación único de personas físicas nacionales es:

*0P-TTTT-AAAA*

Donde 

=======  ============
Dígito   Descripción 
=======  ============
0        Primera posición de la cédula de identidad
P        Provincia
TTTT     Tomo justificado con ceros a la izquierda
AAAA     Número de Asiento justificado con ceros a la izquierda
=======  ============

Un número de cédula válido para una persona física nacional sería, por ejemplo, 01-0913-0259. 

Persona Jurídica
###################################

Este tipo de persona tendrá 3 como primera posición de la cédula, de acuerdo con la tabla de naturalezas antes descrita.  Las restantes 9 posiciones deben cumplir con la siguiente codificación:

*3-TTT-CCCCCC*

Donde 

=======  ============
Dígito   Descripción 
=======  ============
3        Primera posición de la cédula
TTTT     Tipo de Persona Jurídica según la codificación del RN
CCCCCC   Corresponde a un consecutivo asignado por el RN
=======  ============

Persona extranjera residente
###################################

El estándar definido por la Dirección General de Migración y Extranjería, para el número de identificación único de personas físicas de origen extranjero residentes en el país (DIMEX), así como el determinado por la Cancillería de la República para las identificaciones de diplomáticos (DIDI), consta de 12 dígitos y está compuesto de la siguiente forma:

*XNNNCCCCCCDV*

Para el DIMEX:

=======  ============
Dígito   Descripción 
=======  ============
X        En el caso del Dimex este número es un uno (1)
NNN      Código internacional de nacionalidad (ISO 3166).
CCCCCC   Cantidad de nacionales de cada país al momento de la inscripción en el caso del DIMEX.
DV       Dígitos verificadores.
=======  ============

En el caso del DIDI:

=======  ============
Dígito   Descripción 
=======  ============
X        En el caso del Didi este número es un cinco (5)
NNN      Código internacional de nacionalidad (ISO 3166).
CCCCCC   Cantidad de diplomáticos de cada país en el caso de los Didi.
DV       Dígitos verificadores.
=======  ============

A partir del 1º de octubre de 2012, el  DIMEX y el DIDI serán los únicos números de identificación válidos para extranjeros en las operaciones que se tramiten por medio de la plataforma del SINPE.


Algoritmos Hash soportados
----------------------------

Para hacer el cálculo del hash de un documento puede utilizar alguno de los siguientes algoritmos. Se recomienda usar Sha512


=======  ============
Número   Descripción 
=======  ============
1        Sha256
2        Sha384
3        Sha512
=======  ============

Código de error del firmador al solicitar una firma
---------------------------------------------------------

=======  ============
Código   Descripción 
=======  ============
1        Solicitud recibida correctamente.
2        Ha ocurrido algún problema al solicitar la firma.
3        Solicitud con campos incompletos.
4        Existe una diferencia no permitida entre la fecha y hora del cliente y la del servidor. La fecha/hora de la solicitud no debe tener una diferencia de más de 60 segundos de la fecha/hora del servidor.
5        La entidad no se encuentra registrada.
6        La entidad se encuentra en estado inactiva.
7        El negocio no pertenece a la entidad solicitante.
8        El tamaño del resumen de la solicitud de firma es inválido, este debe ser mayor a 1 y menor a  250 caracteres.
9        El tamaño de la razón de firma de la solicitud de firma PAdES es inválida, este debe ser mayor a 1 y menor a  125 caracteres.
10       El suscriptor se encuentra desconectado para recibir una solicitud.
11       El formato de la identificación enviado no es válido.
=======  ============

.. note::
    Existen códigos para validación y verificación, pero acá no están disponibles pues no son públicos todavía.

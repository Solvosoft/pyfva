'''
Created on 30 jul. 2017

@author: luis
'''
HASH_METHODS = (
    ('Sha256', 'Sha256'),
    ('Sha256', 'Sha256'),
    ('Sha512', 'Sha512'),
)

ENTIDAD_NO_REGISTRADA = 5

ERRORES_AL_SOLICITAR_FIRMA = (
    (1, 'Solicitud recibida correctamente.'),
    (2, 'Ha ocurrido algún problema al solicitar la firma.'),
    (3, 'Solicitud con campos incompletos.'),
    (4, 'Existe una diferencia no permitida entre la fecha y hora del cliente y la del servidor. La fecha/hora de la solicitud no debe tener una diferencia de más de 60 segundos de la fecha/hora del servidor.'),
    (ENTIDAD_NO_REGISTRADA, 'La entidad no se encuentra registrada.'),
    (6, 'La entidad se encuentra en estado inactiva.'),
    (7, 'El negocio no pertenece a la entidad solicitante.'),
    (8, 'El tamaño del resumen de la solicitud de firma es inválido, este debe ser mayor a 1 y menor a  250 caracteres.'),
    (9, 'El tamaño de la razón de firma de la solicitud de firma PAdES es inválida, este debe ser mayor a 1 y menor a  125 caracteres.'),
    (10, 'El suscriptor se encuentra desconectado para recibir una solicitud.'),
    (11, 'El formato de la identificación enviado no es válido.'),

)

ERRORES_AL_NOTIFICAR_FIRMA = (
    (1, 'Solicitud completada sin errores.'),
    (2, 'Ha ocurrido algún problema al firmar.'),
    (3, 'Solicitud de firma rechazada por el suscriptor.'),
    (4, 'El suscriptor ha excedido el tiempo máximo permitido para firmar la solicitud.'),
    (5, 'El suscriptor se encuentra desconectado para recibir una solicitud de firma.'),
    (6, 'El documento XML de la solicitud contiene una marca de bytes (BOM) no permitido.'),
    (7, 'El documento de la solicitud es inválido.'),
    (8, 'El documento de la solicitud contiene firmas.'),
    (9, 'El hash de la solicitud es incorrecto.'),
    (10, 'El certificado del suscriptor está revocado.'),
    (11, 'El certificado del suscriptor está vencido.'),
    (12, 'Existe una solicitud de firma en proceso para el cliente.'),
    (13, 'No se pudo notificar a la entidad.'),
    (14, 'El código de verificación es incorrecto'),
    (15, 'El suscriptor bloqueo el pin de la tarjeta'),
)

ERRORES_VALIDA_CERTIFICADO = (
    (1, 'Certificado válido.'),
    (2, 'Error interno al validar el certificado.'),
    (3, 'Los bytes enviados no corresponden a  un certificado.'),
    (4, 'El certificado del suscriptor está vencido.'),
    (5, 'El certificado del suscriptor está revocado.'),
    (6, 'El Certificado enviado no es de confianza porque no es emitido  por la CA Raíz Nacional.'),
    (7, 'El certificado enviado no es de autenticación.'),
    (8, 'El certificado tiene un problema de estructura, no cuenta con el oid  de ocsp en el que se encuentra la dirección del servicio.'),
    (9, 'El certificado tiene un problema de estructura, no cuenta con los usos de la clave necesarios para un certificado de autenticación.'),
    (10, 'El certificado tiene un problema de estructura, el campo  CN del sujeto tiene una estructura inválida.'),
    (11, 'El certificado tiene un problema de estructura, el campo  SERIALNUMBER del sujeto tiene una estructura inválida.'),
    (12, 'La entidad no se encuentra registrada.'),
    (13, 'La entidad no se encuentra en estado inactiva.')
)

ERRORES_VALIDA_DOCUMENTO = (
    (1, 'Documento válido.'),
    (2, 'Error interno al validar el documento.'),
    (3, 'La entidad no se encuentra registrada.'),
    (4, 'La entidad se encuentra en estado inactiva.'),
    (5, 'El documento no es un XML válido.'),
    (6, 'El documento XML no se encuentra firmado.'),
    (7, 'La firma con id [Identificador de la firma] no contiene el tag QualifyingProperties o no se ha definido el prefijo Etsi [http://uri.etsi.org/01903/v1.3.2#].'),
    (8, 'La firma con id [Identificador de la firma] contiene una estructura no valida.'),
    (9, 'La firma con id [Identificador de la firma] contiene un certificado firmante con un formato no válido.'),
    (10, 'La firma con id [Identificador de la firma] contiene [Cantidad de certificados] certificados con un formato no válido.'),
    (11,
     'La firma con id [Identificador de la firma] contiene una respuesta OCSP no válida.'),
    (12,
     'La estampa de tiempo de la firma con id [Identificador de la firma] no es válida.'),
    (13,
     'La segunda estampa de la firma con id [Identificador de la firma] tiempo no es válida.'),
    (14, 'La firma con id [Identificador de la firma] contiene [Cantidad de  CRL\'s] certificados CRL\'s con un formato no válido.'),
    (15,
     'No se encontró la referencia que apunta al elemento KeyInfo en la firma con id [Identificador de la firma].'),
    (16,
     'No se encontró la referencia que apunta al elemento SignedProperties en la firma con id [Identificador de la firma].'),
    (17,
     'No se encontró la referencia que apunta al documento original en la firma con id [Identificador de la firma].'),
    (18, 'La firma con id [Identificador de la firma] no contiene el tag Transform en la referencia al documento original.'),
    (19, 'La firma con id [Identificador de la firma] no cuenta con el atributo Type en la referencia a las propiedades firmadas.'),
    (20,
     'El atributo Type no debe estar dentro de la referencia que apunta al documento original en la firma con id [Identificador de la firma].'),
    (21,
     'El atributo Type no debe estar dentro de la referencia que apunta a la sección KeyInfo en la firma con id [Identificador de la firma].'),
    (22,
     'El elemento Transform no debe estar dentro de la referencia que apunta a SignedProperties en la firma con id [Identificador de la firma].'),
    (23,
     'El elemento Transform no debe estar dentro de la referencia que apunta a la sección KeyInfo en la firma con id [Identificador de la firma].'),
    (24, 'En la firma con id [Identificador de la firma] el DigestValue de la referencia relacionada con el elemento KeyInfo no coincide.'),
    (25, 'En la firma con id [Identificador de la firma] el DigestValue de la referencia relacionada con el elemento SignedProperties no coincide.'),
    (26, 'En la firma con id [Identificador de la firma] el DigestValue de la referencia relacionada con el documento original no coincide.'),
)

ERRORES_EN_DOCUMENTO = (
    ('SinErrores', 'Sin Errores'),
    ('ProblemasAlValidar', 'Problemas Al Validar'),
    ('EntidadNoSeEncuentraRegistrada', 'Entidad No Se Encuentra Registrada'),
    ('EntidadSeEncuentraInactiva', 'Entidad Se Encuentra Inactiva'),
    ('DocumentoXmlInvalido', 'Documento Xml Invalido'),
    ('DocumentoXmlNoFirmado', 'Documento Xml No Firmado'),
    ('DocumentoXmlSinQualifyingProperties',
     'Documento Xml Sin Qualifying Properties'),
    ('DocumentoXmlConEstructuraInvalida', 'Documento Xml Con Estructura Invalida'),
    ('CertificadoFirmanteNoValido', 'Certificado Firmante No Valido'),
    ('CertificadosNoValidos', 'Certificados No Validos'),
    ('RespuestaOcspNoValida', 'Respuesta Ocsp No Valida'),
    ('EstampaDeTiempoDeFirmaNoValida', 'Estampa De Tiempo De Firma No Valida'),
    ('SegundaEstampaDeTiempoNoValida', 'Segunda Estampa De Tiempo No Valida'),
    ('CrlsNoValidos', 'Crls No Validos'),
    ('ReferenciaKeyInfoNoExiste', 'Referencia Key Info No Existe'),
    ('ReferenciaPropiesdadesFirmadasNoExiste',
     'Referencia Propiesdades Firmadas No Existe'),
    ('ReferenciaDocumentoOriginalNoExiste',
     'Referencia Documento Original No Existe'),
    ('ReferenciaADocumentoOriginalSinTransform',
     'Referencia A Documento Original Sin Transform'),
    ('ReferenciaAPropiedadesFirmadasSinType',
     'Referencia A Propiedades Firmadas Sin Type'),
    ('ReferenciaDocumentoConType', 'Referencia Documento Con Type'),
    ('ReferenciaKeyInfoConType', 'Referencia Key Info Con Type'),
    ('ReferenciaSignedPropertiesConTransform',
     'Referencia Signed Properties Con Transform'),
    ('ReferenciaKeyInfoConTransform', 'Referencia Key Info Con Transform'),
    ('HashReferenciaKeyInfoNoCoincide', 'Hash Referencia Key Info No Coincide'),
    ('HashReferenciaPropiedadesFirmadasNoCoincide',
     'Hash Referencia Propiedades Firmadas No Coincide'),
    ('HashReferenciaDocumentoOriginalNoCoincide',
     'Hash Referencia Documento Original No Coincide'),
    ('SignatureValueNoValido', 'Signature Value No Valido'),
    ('KeyValueNoCoincideConLlavePublica',
     'Key Value No Coincide Con Llave Publica'),
    ('OcspNoAsociadaACertificado', 'Ocsp No Asociada A Certificado'),
    ('CertificadoFirmanteRevocado', 'Certificado Firmante Revocado'),
    ('CertificadoFirmanteEstadoDesconocido',
     'Certificado Firmante Estado Desconocido'),
    ('CertificadoFirmanteVencido', 'Certificado Firmante Vencido'),
    ('TipoDeCertificadoFirmanteNoValido', 'Tipo De Certificado Firmante No Valido'),
    ('QualifyingPropertiesContraIdSignature',
     'Qualifying Properties Contra Id Signature'),
    ('SerialNumberNoCoincide', 'Serial Number No Coincide'),
    ('IssuerNameNoCoincide', 'Issuer Name No Coincide'),
    ('MimeTypeNoPermitido', 'Mime Type No Permitido'),
    ('MimeTypeCadenaNoValida', 'Mime Type Cadena No Valida'),
    ('EncodingNoPermitido', 'Encoding No Permitido'),
    ('CantidadDataObjectFormatIncorrecta',
     'Cantidad Data Object Format Incorrecta'),
    ('DataObjectFormatNoValido', 'Data Object Format No Valido'),
    ('HashCertificadoFirmanteNoCoincide', 'Hash Certificado Firmante No Coincide'),
    ('SigningTimeFormatoNoValido', 'Signing Time Formato No Valido'),
    ('EstampaDeTiempoDeFirmaIntegridadComprometida',
     'Estampa De Tiempo De Firma Integridad Comprometida'),
    ('CertificadoDeEstampaDeFirmaNoCoincide',
     'Certificado De Estampa De Firma No Coincide'),
    ('SegundaEstampaDeTiempoIntegridadComprometida',
     'Segunda Estampa De Tiempo Integridad Comprometida'),
    ('CertificadoDeSegundaEstampaNoCoincide',
     'Certificado De Segunda Estampa No Coincide'),
    ('CantidadDeReferenciasACertificadosIncorrecta',
     'Cantidad De Referencias A Certificados Incorrecta'),
    ('ReferenciaACertificadoNoValida', 'Referencia A Certificado No Valida'),
    ('NumeroDeSerieNoCoincide', 'Numero De Serie No Coincide'),
    ('CompleteCertRefsEmisoresDistintos', 'Complete Cert Refs Emisores Distintos'),
    ('ResponderIdIncorrecto', 'Responder Id Incorrecto'),
    ('ByKeyNoCoincideConLlaveOcsp', 'By Key No Coincide Con Llave Ocsp'),
    ('ByNameNoCoincideConLlaveOcsp', 'By Name No Coincide Con Llave Ocsp'),
    ('CantidadDeReferenciasOcspIncorrecta',
     'Cantidad De Referencias Ocsp Incorrecta'),
    ('ReferenciaAOcspNoValida', 'Referencia A Ocsp No Valida'),
    ('ProduceAtDeOcspIncorrecto', 'Produce At De Ocsp Incorrecto'),
    ('CantidadDeReferenciasCrlIncorrecta',
     'Cantidad De Referencias Crl Incorrecta'),
    ('ReferenciaACrlNoValida', 'Referencia A Crl No Valida'),
    ('IssuerDeCrlIncorrecto', 'Issuer De Crl Incorrecto'),
    ('IssueTimeDeCrlIncorrecto', 'Issue Time De Crl Incorrecto'),
    ('NumeroDeCrlIncorrecto', 'Numero De Crl Incorrecto'),
    ('JerarquiaDeCertificadoFirmanteIncompleta',
     'Jerarquia De Certificado Firmante Incompleta'),
    ('JerarquiaDeCertificadoFirmanteNoValida',
     'Jerarquia De Certificado Firmante No Valida'),
    ('JerarquiaDeCertificadoHojaIncompleta',
     'Jerarquia De Certificado Hoja Incompleta'),
    ('JerarquiaDeCertificadoHojaNoValida',
     'Jerarquia De Certificado Hoja No Valida'),
    ('CertificadoTSANoIncluido', 'Certificado T S A No Incluido'),
    ('CertificadoOcspNoIncluido', 'Certificado Ocsp No Incluido'),
    ('CertificadoExtra', 'Certificado Extra'),
    ('CertificadoSinCRL', 'Certificado Sin C R L'),
    ('CertificadoRevocado', 'Certificado Revocado'),
    ('CertificadoVencido', 'Certificado Vencido'),
    ('CertificadoOcspNoCoincide', 'Certificado Ocsp No Coincide'),
    ('RespuestaOcspFueraDeLasEstampas', 'Respuesta Ocsp Fuera De Las Estampas'),
    ('CrlVencido', 'Crl Vencido'),
    ('CrlNoValido', 'Crl No Valido'),
    ('CrlDeltaYBaseNoIncluidos', 'Crl Delta Y Base No Incluidos'),
    ('CrlExtra', 'Crl Extra'),
    ('CrlIndicatorNoValido', 'Crl Indicator No Valido'),
    ('FirmaSinPrefijo', 'Firma Sin Prefijo'),

)


ERRORES_VERIFICACION = (
    (0, 'Verificación recibida correctamente.'),
    (1, 'Ha ocurrido algún problema al verificar el estado de la firma.'),
    (2, 'La entidad no se encuentra registrada.'),
    (3, 'La entidad se encuentra en estado inactiva.')
)


def get_text_representation(error, code):
    errors = dict(error)
    if code in errors:
        return errors[code]
    return ''


def span_text(text, max_char=48):
    needed = max_char - len(text)
    dev = text
    if needed:
        dev = text + " " * needed
    return dev


def show_constants():
    # use como python -c "from pyfva.constants import
    # show_constants;print(show_constants())" >
    # ./docs/source/formatos_en_fva.rst
    __doc__ = """
Códigos usados en pyfva
=========================

.. note:: 
    Los códigos aquí descritos son los usados por pyFVA pero no son los oficiales del FVA del BCCR ya que todavía no son públicos, aún así se intenta
    ser 100%% compatible con los códigos oficiales, por lo que estos son una buena referencia


HASH_METHODS
---------------

=======\t============
Código\tDescripción 
=======\t============
%s
=======\t============

ERRORES_AL_SOLICITAR_FIRMA
----------------------------

=======\t============
Código\tDescripción 
=======\t============
%s
=======\t============

ERRORES_AL_NOTIFICAR_FIRMA
----------------------------

=======\t============
Código\tDescripción 
=======\t============
%s
=======\t============


ERRORES_VALIDA_CERTIFICADO
----------------------------

=======\t============
Código\tDescripción 
=======\t============
%s
=======\t============

ERRORES_VALIDA_DOCUMENTO
--------------------------

=======\t============
Código\tDescripción 
=======\t============
%s
=======\t============

ERRORES_EN_DOCUMENTO
----------------------

===============================================\t============
Código\tDescripción 
===============================================\t============
%s
===============================================\t============

    """ % ("\n".join(["%s\t%s" % (x, y) for x, y in HASH_METHODS]),
           "\n".join(["%s\t%s" % (x, y)
                      for x, y in ERRORES_AL_SOLICITAR_FIRMA]),
           "\n".join(["%s\t%s" % (x, y)
                      for x, y in ERRORES_AL_NOTIFICAR_FIRMA]),
           "\n".join(["%s\t%s" % (x, y)
                      for x, y in ERRORES_VALIDA_CERTIFICADO]),
           "\n".join(["%s\t%s" % (x, y) for x, y in ERRORES_VALIDA_DOCUMENTO]),
           "\n".join(["%s\t%s" % (span_text(x), y)
                      for x, y in ERRORES_EN_DOCUMENTO]),
           )
    return __doc__

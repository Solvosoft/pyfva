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
    (8, 'El tamaño del resumen de la solicitud de firma es no valido, este debe ser mayor a 1 y menor a  250 caracteres.'),
    (9, 'El tamaño de la razón de firma de la solicitud de firma PAdES es inválida, este debe ser mayor a 1 y menor a  125 caracteres.'),
    (10, 'El suscriptor se encuentra desconectado para recibir una solicitud.'),
    (11, 'El formato de la identificación enviado no es válido.')
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
    (16, 'El documento no es válido para ser contrafirmado.')
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

ERRORES_VALIDAR_XMLCOFIRMA=(
(1 , 'Documento válido.'),
(2 , 'Error interno al validar el documento.'),
(3 , 'La entidad no se encuentra registrada.'),
(4 , 'La entidad se encuentra en estado inactiva.'),
(5 , 'El documento no es un XML válido.'),
(6 , 'El documento XML no se encuentra firmado.'),
(7 , 'La firma con id [Identificador de la firma] no contiene el tag QualifyingProperties o no se ha definido el prefijo Etsi [http://uri.etsi.org/01903/v1.3.2#].'),
(8 , 'La firma con id [Identificador de la firma] contiene una estructura no valida.'),
(9 , 'La firma con id [Identificador de la firma] contiene un certificado firmante con un formato no válido.'),
(10 , 'La firma con id [Identificador de la firma] contiene [Cantidad de certificados] certificados con un formato no válido.'),
(11 , 'La firma con id [Identificador de la firma] contiene una respuesta OCSP no válida.'),
(12 , 'La estampa de tiempo de la firma con id [Identificador de la firma] no es válida.'),
(13 , 'La segunda estampa de la firma con id [Identificador de la firma] tiempo no es válida.'),
(14 , 'La firma con id [Identificador de la firma] contiene [Cantidad de  CRL\'s] certificados CRL\'s con un formato no válido.'),
(15 , 'No se encontró la referencia que apunta al elemento KeyInfo en la firma con id [Identificador de la firma].'),
(16 , 'No se encontró la referencia que apunta al elemento SignedProperties en la firma con id [Identificador de la firma].'),
(17 , 'No se encontró la referencia que apunta al documento original en la firma con id [Identificador de la firma].'),
(18 , 'La firma con id [Identificador de la firma] no contiene el tag Transform en la referencia al documento original.'),
(19 , 'La firma con id [Identificador de la firma] no cuenta con el atributo Type en la referencia a las propiedades firmadas.'),
(20 , 'El atributo Type no debe estar dentro de la referencia que apunta al documento original en la firma con id [Identificador de la firma].'),
(21 , 'El atributo Type no debe estar dentro de la referencia que apunta a la sección KeyInfo en la firma con id [Identificador de la firma].'),
(22 , 'El elemento Transform no debe estar dentro de la referencia que apunta a SignedProperties en la firma con id [Identificador de la firma].'),
(23 , 'El elemento Transform no debe estar dentro de la referencia que apunta a la sección KeyInfo en la firma con id [Identificador de la firma].'),
(24 , 'En la firma con id [Identificador de la firma] el DigestValue de la referencia relacionada con el elemento KeyInfo no coincide.'),
(25 , 'En la firma con id [Identificador de la firma] el DigestValue de la referencia relacionada con el elemento SignedProperties no coincide.'),
(26 , 'En la firma con id [Identificador de la firma] el DigestValue de la referencia relacionada con el documento original no coincide.'),
(27 , 'En la firma con id [Identificador de la firma] el valor de la firma en el tag SignatureValue, no coincide con los elementos firmados del elemento SignedInfo, puede ser que la integridad del documento haya sido comprometida.'),
(28 , 'En la firma con id [Identificador de la firma] los valores indicados en el elemento KeyValue no coinciden con la llave pública del certificado.'),
(29 , 'En la firma con id [Identificador de la firma] la respuesta OCSP del documento no coincide con el certificado firmante.'),
(30 , 'En la firma con id [Identificador de la firma] el certificado firmante se encontraba revocado al momento de realizar la firma.'),
(31 , 'En la firma con id [Identificador de la firma] el certificado firmante tenía un formato no válido al momento de realizar la firma.'),
(32 , 'En la firma con id [Identificador de la firma] el certificado firmante se encontraba vencido al momento de realizar la firma según la hora del servidor de estampa de tiempo.'),
(33 , 'En la firma con id [Identificador de la firma] se usó un tipo de certificado no válido para realizar la firma.'),
(34 , 'En la firma con id [Identificador de la firma] el Target del elemento QualifyingProperties no coincide con el atributo id del tag Signature.'),
(35 , 'En la firma con id [Identificador de la firma] el SerialNumber de la sección SignedProperties no coincide con el del certificado firmante.'),
(36 , 'En la firma con id [Identificador de la firma] el IssuerName de la sección SignedProperties no coincide con el del certificado firmante.'),
(37 , 'En la firma con id [Identificador de la firma] algún elemento MimeType no está dentro de los permitidos.'),
(38 , 'En la firma con id [Identificador de la firma] el MimeType utilizado sobrepasa la longitud máxima de caracteres (90 caracteres).'),
(39 , 'En la firma con id [Identificador de la firma] algún encoding no está dentro de los permitidos.'),
(40 , 'En la firma con id [Identificador de la firma] la cantidad de DataObjectFormat es incorrecta.'),
(41 , 'En la firma con id [Identificador de la firma] algún elemento DataObjectFormat referencia a un elemento no válido en la sección SignedInfo.'),
(42 , 'En la firma con id [Identificador de la firma] el resumen hash del elemento DigestValue de la sección SignedProperties, no coincide con el del certificado firmante.'),
(43 , 'En la firma con id [Identificador de la firma] el formato de la fecha/hora indicado en el SigningTime, debe estar en el formato UTC.'),
(44 , 'En la firma con id [Identificador de la firma] la integridad de la estampa de tiempo de la firma está comprometida.'),
(45 , 'En la firma con id [Identificador de la firma] el certificado de la TSA contenido en la primera estampa de tiempo no coincide con el que se encuentra en el elemento CertificateValues.'),
(46 , 'En la firma con id [Identificador de la firma] la integridad de la segunda estampa de tiempo está comprometida.'),
(47 , 'En la firma con id [Identificador de la firma] el certificado de la TSA contenido en la segunda estampa de tiempo no coincide con el que se encuentra en el elemento CertificateValues.'),
(48 , 'En la firma con id [Identificador de la firma] el número de referencias indicadas en el elemento CompleteCertificateRefs, no concuerda con la cantidad de certificados indicado en el elemento de CertificateValues.'),
(49 , 'En la firma con id [Identificador de la firma] existe una referencia en el elemento CompleteCertificateRefs, que no coincide con ningún certificado de la sección CertificateValues.'),
(50 , 'En la firma con id [Identificador de la firma] el SerialNumber [Serial Number] de la sección CompleteCertificateRefs, no coincide con el SerialNumber [Serial Number] del certificado referenciado de la sección CertificateValues.'),
(51 , 'En la firma con id [Identificador de la firma] el IssuerName  [Nombre del emisor] de la sección CompleteCertificateRefs, no coincide con el emisor [Nombre del emisor] del certificado referenciado de la sección CertificateValues.'),
(52 , 'En la firma con id [Identificador de la firma] el tag ResponderID debe contener al menos un elemento ByKey o un elemento ByName.'),
(53 , 'En la firma con id [Identificador de la firma] el valor indicado en el elemento ByKey, no coincide con el hash de la llave pública  del certificado de OCSP.'),
(54 , 'En la firma con id [Identificador de la firma] el valor indicado en el elemento ByName, no coincide con el valor del campo CN del Subject del certificado de OCSP.'),
(55 , 'En la firma con id [Identificador de la firma] el número de referencias indicadas en el elemento de OcspRefs, no concuerdan con la cantidad de datos de revocación indicados en el elemento OcspValues.'),
(56 , 'En la firma con id [Identificador de la firma] existe una referencia en el elemento OCSPRef, que no coincide con ningún dato de revocación de la sección OCSPValues.'),
(57 , 'En la firma con id [Identificador de la firma] el valor del elemento ProduceAT, no coincide con el de la respuesta OCSP.'),
(58 , 'En la firma con id [Identificador de la firma] el número de referencias indicadas en el elemento de CrlRefs, no concuerdan con la cantidad de datos de revocación indicados en el elemento CrlValues.'),
(59 , 'En la firma con id [Identificador de la firma] existe una referencia en el elemento CRLRef, que no coincide con ningún dato de revocación de la sección CRLValues.'),
(60 , 'En la firma con id [Identificador de la firma] un elemento Issuer de la sección CRLRef no coincide con el emisor del CRL referenciado en la sección CRLValues.'),
(61 , 'En la firma con id [Identificador de la firma] un elemento IssueTime de la sección CRLRef, no coincide con el CRL referenciado en la sección CRLValues.'),
(62 , 'En la firma con id [Identificador de la firma] un elemento Number  de la sección CRLRef, no coincide con el CRL referenciado en la sección CRLValues.'),
(63 , 'En la firma con id [Identificador de la firma] no se incluyó la totalidad de los certificados que componen la cadena de la jerarquía nacional del certificado del firmante.'),
(64 , 'En la firma con id [Identificador de la firma] la jerarquía que emitió el certificado del firmante [Cn del sujeto del certificado raíz] no es válida en Costa Rica.'),
(65 , 'En la firma con id [Identificador de la firma] no se incluyó la totalidad de los certificados que componen la cadena de la jerarquía nacional del certificado de [firma, Tsa, Ocsp].'),
(66 , 'En la firma con id [Identificador de la firma] la jerarquía que emitió el certificado de [firma, Tsa, Ocsp] [Cn de la raíz que no es validad] no es válida en Costa Rica.'),
(67 , 'En la firma con id [Identificador de la firma] no se encontró  el certificado de TSA necesario para validar la firma.'),
(68 , 'En la firma con id [Identificador de la firma] no se encontró el certificado de OCSP necesario para validar la firma.'),
(69 , 'En la firma con id [Identificador de la firma] se encontraron certificados de más los cuales no son necesarios para la validación de la firma.'),
(70 , 'En la firma con id [Identificador de la firma] para el certificado [Cn del sujeto del certificado] no se encontró un CRL para verificar si estaba revocado en el momento de la firma.'),
(71 , 'En la firma con id [Identificador de la firma] el certificado  certificado [Cn del sujeto del certificado] estaba revocado en el momento de la firma.'),
(72 , 'En la firma con id [Identificador de la firma] el certificado  certificado [Cn del sujeto del certificado] estaba vencido en el momento de la firma.'),
(73 , 'En la firma con id [Identificador de la firma] el certificado contenido en la respuesta OCSP, no coincide con el que se encuentra en el elemento CertificateValues.'),
(74 , 'En la firma con id [Identificador de la firma] la respuesta OCSP no se encontraba válida en el momento de la firma.'),
(75 , 'En la firma con id [Identificador de la firma] alguno de los CRLs no se encontraban válidos en el momento de la firma.'),
(76 , 'En la firma con id [Identificador de la firma] alguno de los CRLs no fueron emitidos por una CA de la jerarquía nacional.'),
(77 , 'En la firma con id [Identificador de la firma] no existen los CRLs necesarios para validar la revocación del certificado firmante. Debe incluirse el CRL Base y el CRL Delta.'),
(78 , 'En la firma con id [Identificador de la firma] se encontraron CRLs de más, los cuales no son necesarios para la validación de la revocación.'),
(79 , 'En la firma con id [Identificador de la firma] el CRLIndicator del Crl Delta es mayor el CrlNumber del Crl Base.'),
(80 , 'Para la firma con id [Identificador de la firma] no se ha definido el prefijo DS [http://www.w3.org/2000/09/xmldsig#].'),
)

ERRORES_VALIDAR_XMLCONTRAFIRMA=(
(0, 'Documento válido.'),
(1, 'Error interno al validar el documento.'),
(2, 'La entidad no se encuentra registrada.'),
(3, 'La entidad se encuentra en estado inactiva.'),
(4, 'El documento no es un XML válido.'),
(5, 'El documento XML no se encuentra firmado.'),
(6, 'La firma con id [Identificador de la firma] no contiene el tag QualifyingProperties o no se ha definido el prefijo Etsi [http://uri.etsi.org/01903/v1.3.2#].'),
(7, 'La firma con id [Identificador de la firma] contiene una estructura no valida.'),
(8, 'La firma con id [Identificador de la firma] contiene un certificado firmante con un formato no válido.'),
(9, 'La firma con id [Identificador de la firma] contiene [Cantidad de certificados] certificados con un formato no válido.'),
(10, 'La firma con id [Identificador de la firma] contiene una respuesta OCSP no válida.'),
(11, 'La estampa de tiempo de la firma con id [Identificador de la firma] no es válida.'),
(12, 'La segunda estampa de la firma con id [Identificador de la firma] tiempo no es válida.'),
(13, 'La firma con id [Identificador de la firma] contiene [Cantidad de  CRL\'s] certificados CRL\'s con un formato no válido.'),
(14, 'No se encontró la referencia que apunta al elemento KeyInfo en la firma con id [Identificador de la firma].'),
(15, 'No se encontró la referencia que apunta al elemento SignedProperties en la firma con id [Identificador de la firma].'),
(16, 'No se encontró la referencia que apunta al documento original en la firma con id [Identificador de la firma].'),
(17, 'La firma con id [Identificador de la firma] no contiene el tag Transform en la referencia al documento original.'),
(18, 'La firma con id [Identificador de la firma] no cuenta con el atributo Type en la referencia a las propiedades firmadas.'),
(19, 'El atributo Type no debe estar dentro de la referencia que apunta al documento original en la firma con id [Identificador de la firma].'),
(20, 'El atributo Type no debe estar dentro de la referencia que apunta a la sección KeyInfo en la firma con id [Identificador de la firma].'),
(21, 'El elemento Transform no debe estar dentro de la referencia que apunta a SignedProperties en la firma con id [Identificador de la firma].'),
(22, 'El elemento Transform no debe estar dentro de la referencia que apunta a la sección KeyInfo en la firma con id [Identificador de la firma].'),
(23, 'En la firma con id [Identificador de la firma] el DigestValue de la referencia relacionada con el elemento KeyInfo no coincide.'),
(24, 'En la firma con id [Identificador de la firma] el DigestValue de la referencia relacionada con el elemento SignedProperties no coincide.'),
(25, 'En la firma con id [Identificador de la firma] el DigestValue de la referencia relacionada con el documento original no coincide.'),
(26, 'En la firma con id [Identificador de la firma] el valor de la firma en el tag SignatureValue, no coincide con los elementos firmados del elemento SignedInfo, puede ser que la integridad del documento haya sido comprometida.'),
(27, 'En la firma con id [Identificador de la firma] los valores indicados en el elemento KeyValue no coinciden con la llave pública del certificado.'),
(28, 'En la firma con id [Identificador de la firma] la respuesta OCSP del documento no coincide con el certificado firmante.'),
(29, 'En la firma con id [Identificador de la firma] el certificado firmante se encontraba revocado al momento de realizar la firma.'),
(30, 'En la firma con id [Identificador de la firma] el certificado firmante tenía un formato no válido al momento de realizar la firma.'),
(31, 'En la firma con id [Identificador de la firma] el certificado firmante se encontraba vencido al momento de realizar la firma según la hora del servidor de estampa de tiempo.'),
(32, 'En la firma con id [Identificador de la firma] se usó un tipo de certificado no válido para realizar la firma.'),
(33, 'En la firma con id [Identificador de la firma] el Target del elemento QualifyingProperties no coincide con el atributo id del tag Signature.'),
(34, 'En la firma con id [Identificador de la firma] el SerialNumber de la sección SignedProperties no coincide con el del certificado firmante.'),
(35, 'En la firma con id [Identificador de la firma] el IssuerName de la sección SignedProperties no coincide con el del certificado firmante.'),
(36, 'En la firma con id [Identificador de la firma] algún elemento MimeType no está dentro de los permitidos.'),
(37, 'En la firma con id [Identificador de la firma] el MimeType utilizado sobrepasa la longitud máxima de caracteres (90 caracteres).'),
(38, 'En la firma con id [Identificador de la firma] algún encoding no está dentro de los permitidos.'),
(39, 'En la firma con id [Identificador de la firma] la cantidad de DataObjectFormat es incorrecta.'),
(40, 'En la firma con id [Identificador de la firma] algún elemento DataObjectFormat referencia a un elemento no válido en la sección SignedInfo.'),
(41, 'En la firma con id [Identificador de la firma] el resumen hash del elemento DigestValue de la sección SignedProperties, no coincide con el del certificado firmante.'),
(42, 'En la firma con id [Identificador de la firma] el formato de la fecha/hora indicado en el SigningTime, debe estar en el formato UTC.'),
(43, 'En la firma con id [Identificador de la firma] la integridad de la estampa de tiempo de la firma está comprometida.'),
(44, 'En la firma con id [Identificador de la firma] el certificado de la TSA contenido en la primera estampa de tiempo no coincide con el que se encuentra en el elemento CertificateValues.'),
(45, 'En la firma con id [Identificador de la firma] la integridad de la segunda estampa de tiempo está comprometida.'),
(46, 'En la firma con id [Identificador de la firma] el certificado de la TSA contenido en la segunda estampa de tiempo no coincide con el que se encuentra en el elemento CertificateValues.'),
(47, 'En la firma con id [Identificador de la firma] el número de referencias indicadas en el elemento CompleteCertificateRefs, no concuerda con la cantidad de certificados indicado en el elemento de CertificateValues.'),
(48, 'En la firma con id [Identificador de la firma] existe una referencia en el elemento CompleteCertificateRefs, que no coincide con ningún certificado de la sección CertificateValues.'),
(49, 'En la firma con id [Identificador de la firma] el SerialNumber [Serial Number] de la sección CompleteCertificateRefs, no coincide con el SerialNumber [Serial Number] del certificado referenciado de la sección CertificateValues.'),
(50, 'En la firma con id [Identificador de la firma] el IssuerName  [Nombre del emisor] de la sección CompleteCertificateRefs, no coincide con el emisor [Nombre del emisor] del certificado referenciado de la sección CertificateValues.'),
(51, 'En la firma con id [Identificador de la firma] el tag ResponderID debe contener al menos un elemento ByKey o un elemento ByName.'),
(52, 'En la firma con id [Identificador de la firma] el valor indicado en el elemento ByKey, no coincide con el hash de la llave pública  del certificado de OCSP.'),
(53, 'En la firma con id [Identificador de la firma] el valor indicado en el elemento ByName, no coincide con el valor del campo CN del Subject del certificado de OCSP.'),
(54, 'En la firma con id [Identificador de la firma] el número de referencias indicadas en el elemento de OcspRefs, no concuerdan con la cantidad de datos de revocación indicados en el elemento OcspValues.'),
(55, 'En la firma con id [Identificador de la firma] existe una referencia en el elemento OCSPRef, que no coincide con ningún dato de revocación de la sección OCSPValues.'),
(56, 'En la firma con id [Identificador de la firma] el valor del elemento ProduceAT, no coincide con el de la respuesta OCSP.'),
(57, 'En la firma con id [Identificador de la firma] el número de referencias indicadas en el elemento de CrlRefs, no concuerdan con la cantidad de datos de revocación indicados en el elemento CrlValues.'),
(58, 'En la firma con id [Identificador de la firma] existe una referencia en el elemento CRLRef, que no coincide con ningún dato de revocación de la sección CRLValues.'),
(59, 'En la firma con id [Identificador de la firma] un elemento Issuer de la sección CRLRef no coincide con el emisor del CRL referenciado en la sección CRLValues'), 
(60, 'En la firma con id [Identificador de la firma] un elemento IssueTime de la sección CRLRef, no coincide con el CRL referenciado en la sección CRLValues.'),
(61, 'En la firma con id [Identificador de la firma] un elemento Number  de la sección CRLRef, no coincide con el CRL referenciado en la sección CRLValues.'),
(62, 'En la firma con id [Identificador de la firma] no se incluyó la totalidad de los certificados que componen la cadena de la jerarquía nacional del certificado del firmante.'),
(63, 'En la firma con id [Identificador de la firma] la jerarquía que emitió el certificado del firmante [Cn del sujeto del certificado raíz] no es válida en Costa Rica.'),
(64, 'En la firma con id [Identificador de la firma] no se incluyó la totalidad de los certificados que componen la cadena de la jerarquía nacional del certificado de [firma, Tsa, Ocsp].'),
(65, 'En la firma con id [Identificador de la firma] la jerarquía que emitió el certificado de [firma, Tsa, Ocsp] [Cn de la raíz que no es validad] no es válida en Costa Rica.'),
(66, 'En la firma con id [Identificador de la firma] no se encontró  el certificado de TSA necesario para validar la firma.'),
(67, 'En la firma con id [Identificador de la firma] no se encontró el certificado de OCSP necesario para validar la firma.'),
(68, 'En la firma con id [Identificador de la firma] se encontraron certificados de más los cuales no son necesarios para la validación de la firma.'),
(69, 'En la firma con id [Identificador de la firma] para el certificado [Cn del sujeto del certificado] no se encontró un CRL para verificar si estaba revocado en el momento de la firma.'),
(70, 'En la firma con id [Identificador de la firma] el certificado  certificado [Cn del sujeto del certificado] estaba revocado en el momento de la firma.'),
(71, 'En la firma con id [Identificador de la firma] el certificado  certificado [Cn del sujeto del certificado] estaba vencido en el momento de la firma.'),
(72, 'En la firma con id [Identificador de la firma] el certificado contenido en la respuesta OCSP, no coincide con el que se encuentra en el elemento CertificateValues.'),
(73, 'En la firma con id [Identificador de la firma] la respuesta OCSP no se encontraba válida en el momento de la firma.'),
(74, 'En la firma con id [Identificador de la firma] alguno de los CRLs no se encontraban válidos en el momento de la firma.'),
(75, 'En la firma con id [Identificador de la firma] alguno de los CRLs no fueron emitidos por una CA de la jerarquía nacional.'),
(76, 'En la firma con id [Identificador de la firma] no existen los CRLs necesarios para validar la revocación del certificado firmante. Debe incluirse el CRL Base y el CRL Delta.'),
(77, 'En la firma con id [Identificador de la firma] se encontraron CRLs de más, los cuales no son necesarios para la validación de la revocación.'),
(78, 'En la firma con id [Identificador de la firma] el CRLIndicator del Crl Delta es mayor el CrlNumber del Crl Base.'),
(79, 'Para la firma con id [Identificador de la firma] no se ha definido el prefijo DS [http://www.w3.org/2000/09/xmldsig#].'),
(80, 'No se encontró la referencia que apunta al elemento SignatureValue en la Contra Firma con id [Identificador de la firma].'),
(81, 'La firma con el id [Identificador de la firma] no cuenta con el atributo Type en la referencia al SignatureValue de la firma anterior.'),
(82, 'En la firma con id [Identificador de la firma] el DigestValue de la referencia al SignatureValue de la firma anterior no coincide.')    
)


ERRORES_VALIDAR_MSOFFICE=(
(0, 'Documento válido.'),
(1, 'Error interno al validar el documento.'),
(2, 'La entidad enviada no se encuentra registrada.'),
(3, 'La entidad enviada se encuentra en estado Inactiva.'),
(4, 'El documento no es un XML válido.'),
(5, 'El documento no se encuentra firmado.'),
(6, 'La firma [Identificador de la firma] no contiene el tag QualifyingProperties o no se ha definido el prefijo Etsi [http://uri.etsi.org/01903/v1.3.2#].'),
(7, 'La firma [Identificador de la firma] contiene una estructura no valida.'),
(8, 'La firma [Identificador de la firma] contiene un certificado firmante con un formato no válido.'),
(9, 'La firma [Identificador de la firma] contiene [Cantidad de certificados] certificados con un formato no válido.'),
(10, 'La firma [Identificador de la firma] contiene una respuesta OCSP no válida.'),
(11, 'La estampa de tiempo de la firma [Identificador de la firma] no es válida.'),
(12, 'La segunda estampa de tiempo de la firma [Identificador de la firma] no es válida.'),
(13, 'La firma [Identificador de la firma] contiene [Cantidad de  CRL\'s] CRL\'s con un formato no válido.'),
(14, 'No se encontró la referencia que apunta al elemento Manifest en la firma [Identificador de la firma].'),
(15, 'La firma {0} no cuenta con el atributo Type en la referencia de relación.'),
(16, 'No se encontró la referencia que apunta al elemento SignedProperties en la firma [Identificador de la firma].'),
(17, 'No se encontró la referencia del documento en la firma [Identificador de la firma].'),
(18, 'La firma [Identificador de la firma] no cuenta con el atributo Type en la referencia a las propiedades firmadas.'),
(19, 'La firma [Identificador de la firma] cuenta un atributo Type inválido en la referencia a las propiedades firmadas.'),
(20, 'La firma [Identificador de la firma] no cuenta con un atributo Transform en la referencia a las propiedades firmadas invalido.'),
(21, 'El elemento Transform no debe estar dentro de la referencia que apunta a la sección KeyInfo en la firma [Identificador de la firma].'),
(22, 'El elemento Transform no debe estar dentro de la referencia que apunta a la sección Manifest en la firma [Identificador de la firma].'),
(23, 'En la firma [Identificador de la firma] las propiedades firmadas tienen un algoritmo de transformación no válido.'),
(24, 'En la firma [Identificador de la firma] el DigestValue de la referencia relacionada con el elemento SignedProperties no coincide.'),
(25, 'En la firma [Identificador de la firma] el DigestValue de la referencia relacionada con el elemento Manifest no coincide.'),
(26, 'En la firma [Identificador de la firma] el DigestValue de la referencia relacionada con el elemento OfficeObject no coincide.'),
(27, 'En la firma [Identificador de la firma] el DigestValue de la referencia de parte del documento [Uri] en el elemento Manifest no coincide.'),
(28, 'En la firma [Identificador de la firma] el DigestValue de la referencia del documento en el elemento Manifest no coincide.'),
(29, 'En la firma [Identificador de la firma] el valor de la firma en el tag SignatureValue, no coincide con los elementos firmados del elemento SignedInfo, puede ser que la integridad del documento haya sido comprometida.'),
(30, 'En la firma [Identificador de la firma] la respuesta OCSP del documento no coincide con el certificado firmante.'),
(31, 'En la firma [Identificador de la firma] el certificado firmante se encontraba revocado al momento de realizar la firma.'),
(32, 'En la firma [Identificador de la firma] el certificado firmante tenía un formato no válido al momento de realizar la firma.'),
(33, 'En la firma [Identificador de la firma] el certificado firmante se encontraba vencido al momento de realizar la firma según la hora del servidor de estampa de tiempo.'),
(34, 'En la firma [Identificador de la firma] se usó un tipo de certificado no válido para realizar la firma.'), 
(35, 'En la firma [Identificador de la firma] el Target del elemento QualifyingProperties no coincide con el atributo id del tag Signature.'),
(36, 'En la firma con [Identificador de la firma] el SerialNumber de la sección SignedProperties no coincide con el del certificado firmante.'),
(37, 'En la firma con [Identificador de la firma] el IssuerName de la sección SignedProperties no coincide con el del certificado firmante.'),
(38, 'En la firma [Identificador de la firma] el resumen hash del elemento DigestValue de la sección SignedProperties, no coincide con el del certificado firmante.'),
(39, 'En la firma [Identificador de la firma] el formato de la fecha/hora indicado en el SigningTime, debe estar en el formato UTC.'),
(40, 'En la firma [Identificador de la firma] la integridad de la estampa de tiempo de la firma está comprometida.'),
(41, 'En la firma [Identificador de la firma] el certificado de la TSA contenido en la primera estampa de tiempo no coincide con el que se encuentra en el elemento CertificateValues.'),
(42, 'En la firma [Identificador de la firma] la integridad de la segunda estampa de tiempo está comprometida.'),
(43, 'En la firma [Identificador de la firma] el certificado de la TSA contenido en la segunda estampa de tiempo no coincide con el que se encuentra en el elemento CertificateValues.'),
(44, 'En la firma [Identificador de la firma] el número de referencias indicadas en el elemento CompleteCertificateRefs, no concuerda con la cantidad de certificados indicado en el elemento de CertificateValues.'),
(45, 'En la firma [Identificador de la firma] existe una referencia en el elemento CompleteCertificateRefs, que no coincide con ningún certificado de la sección CertificateValues.'),
(46, 'En la firma [Identificador de la firma] el SerialNumber [Serial Number] de la sección CompleteCertificateRefs, no coincide con el SerialNumber [Serial Number] del certificado referenciado de la sección CertificateValues.'),
(47, 'En la firma [Identificador de la firma] el IssuerName [Issuer Name] de la sección CompleteCertificateRefs, no coincide con el emisor [Emisor] del certificado referenciado de la sección CertificateValues.'),
(48, 'En la firma [Identificador de la firma] el tag ResponderID debe contener al menos un elemento ByKey o un elemento ByName.'),
(49, 'En la firma [Identificador de la firma] el valor indicado en el elemento ByKey, no coincide con el hash de la llave pública  del certificado de OCSP.'),
(50, 'En la firma [Identificador de la firma] el valor indicado en el elemento ByName, no coincide con el valor del campo CN del Subject del certificado de OCSP.'),
(51, 'En la firma [Identificador de la firma] el número de referencias indicadas en el elemento de OcspRefs, no concuerdan con la cantidad de datos de revocación indicados en el elemento OcspValues.'),
(52, 'En la firma [Identificador de la firma] existe una referencia en el elemento OCSPRef, que no coincide con ningún dato de revocación de la sección OCSPValues.'),
(53, 'En la firma [Identificador de la firma] el valor del elemento ProduceAT, no coincide con el de la respuesta OCSP.'),
(54, 'En la firma [Identificador de la firma] el número de referencias indicadas en el elemento de CrlRefs, no concuerdan con la cantidad de datos de revocación indicados en el elemento CrlValues.'),
(55, 'En la firma [Identificador de la firma] existe una referencia en el elemento CRLRef, que no coincide con ningún dato de revocación de la sección CRLValues.'),
(56, 'En la firma [Identificador de la firma] un elemento Issuer de la sección CRLRef no coincide con el emisor del CRL referenciado en la sección CRLValues.'), 
(57, 'En la firma [Identificador de la firma] un elemento IssueTime de la sección CRLRef, no coincide con el CRL referenciado en la sección CRLValues.'),
(58, 'En la firma [Identificador de la firma] un elemento Number  de la sección CRLRef, no coincide con el CRL referenciado en la sección CRLValues.'),
(59, 'En la firma [Identificador de la firma] no se incluyó la totalidad de los certificados que componen la cadena de la jerarquía nacional del certificado del firmante.'),
(60, 'En la firma [Identificador de la firma] la jerarquía que emitió el certificado del firmante no es válida en Costa Rica.'),
(61, 'En la firma [Identificador de la firma] no se incluyó la totalidad de los certificados que componen la cadena de la jerarquía nacional de estampa de tiempo.'),
(62, 'En la firma [Identificador de la firma] la jerarquía que emitió el certificado de estampa de tiempo [Tsa] no es válida en Costa Rica.'),
(63, 'En la firma [Identificador de la firma] no se incluyó la totalidad de los certificados que componen la cadena de la jerarquía nacional del certificado de [Cn del sujeto del certificado].'),
(64, 'En la firma [Identificador de la firma] la jerarquía que emitió el certificado de [firma, Tsa, Ocsp] [Cn de la raíz que no es validad] no es válida en Costa Rica.'),
(65, 'En la firma [Identificador de la firma] se encontraron certificados de más, los cuales no son necesarios para la validación de la firma.'),
(66, 'En la firma [Identificador de la firma] para el certificado [Cn del sujeto del certificado] no se encontró un CRL para verificar si estaba revocado en el momento de la firma.'),
(67, 'En la firma [Identificador de la firma] el certificado [Cn del sujeto del certificado] estaba revocado en el momento de la firma.'),
(68, 'En la firma [Identificador de la firma] el certificado [Cn del sujeto del certificado] estaba vencido en el momento de la firma.'),
(69, 'En la firma [Identificador de la firma] el certificado contenido en la respuesta OCSP, no coincide con el que se encuentra en el elemento CertificateValues.'),
(70, 'En la firma [Identificador de la firma] alguno de los CRLs no se encontraban válidos en el momento de la firma.'),
(71, 'En la firma [Identificador de la firma] alguno de los CRLs no fueron emitidos por una CA de la jerarquía nacional.'),
(72, 'En la firma [Identificador de la firma] no existen los CRLs necesarios para validar la revocación del certificado firmante. Debe incluirse el CRL Base y el CRL Delta.'),
(73, 'En la firma [Identificador de la firma] se encontraron CRLs de más, los cuales no son necesarios para la validación de la revocación.'),
(74, 'En la firma [Identificador de la firma]  el CRLIndicator del Crl Delta es mayor al CrlNumber del Crl Base.'),
(75, 'El documento no es válido.'),
(76, 'En la firma [Identificador de la firma] el formato del SignatureTime es incorrecto.'),
(77, 'En la firma [Identificador de la firma] el formato del valor de la fecha del SignatureTime es incorrecto.'),
(78, 'La firma [Identificador de la firma] no cuenta con el atributo Type en la referencia al Office Object.'),
(79, 'La firma [Identificador de la firma] no cuenta con un atributo Type valido en la referencia a Office Object.'),
(80, 'La firma [Identificador de la firma] no cuenta con un atributo Type valido en la referencia de relación.'),
(81, 'No se encontró la referencia que apunta al elemento Office Object en la firma [Identificador de la firma].')
)


ERRORES_VALIDAR_ODF=(
(0, 'Documento válido.'),
(1, 'Error interno al validar el documento.'),
(2, 'La entidad enviada no se encuentra registrada.'),
(3, 'La entidad enviada se encuentra en estado Inactiva.'),
(4, 'El documento no es un XML válido.'),
(5, 'El documento no se encuentra firmado.'),
(6, 'La firma [Identificador de la firma] no contiene el tag QualifyingProperties o no se ha definido el prefijo Etsi [http://uri.etsi.org/01903/v1.3.2#].'),
(7, 'La firma con id [Identificador de la firma] contiene una estructura no valida.'),
(8, 'La firma con id [Identificador de la firma] contiene un certificado firmante con un formato no válido.'),
(9, 'La firma con id [Identificador de la firma] contiene [Cantidad de certificados]  certificados con un formato no válido.'),
(10, 'La firma con id [Identificador de la firma] contiene una respuesta OCSP no válida.'),
(11, 'La estampa de tiempo de la firma con id [Identificador de la firma] no es válida.'),
(12, 'La segunda estampa de tiempo de la firma con id [Identificador de la firma] no es válida.'),
(13, 'La firma con id [Identificador de la firma] contiene [Cantidad de certificados]  CRL\'s con un formato no válido.'),
(14, 'No se encontró la referencia en la firma con id [Identificador de la firma].'),
(15, 'En la firma con id [Identificador de la firma] el DigestValue de la referencia no coincide.'),
(16, 'La firma [Identificador de la firma] cuenta con un atributo Type no válido en la referencia a las propiedades firmadas.'),
(17, 'No se encontró la referencia que apunta al elemento SignedProperties en la firma con id [Identificador de la firma].'),
(18, 'En la firma con id [Identificador de la firma] el DigestValue de la referencia relacionada con el elemento SignatureProperties no coincide.'),
(19, 'En la firma con id [Identificador de la firma] el DigestValue de la referencia relacionada con el elemento SignedProperties no coincide.'),
(20, 'En la firma con id [Identificador de la firma] el valor de la firma en el tag SignatureValue, no coincide con los elementos firmados del elemento SignedInfo, puede ser que la integridad del documento haya sido comprometida.'),
(21, 'En la firma con id [Identificador de la firma] la respuesta OCSP del documento no coincide con el certificado firmante.'),
(22, 'En la firma con id [Identificador de la firma] el certificado firmante se encontraba revocado al momento de realizar la firma.'),
(23, 'En la firma con id [Identificador de la firma] el certificado firmante tenía un formato no válido al momento de realizar la firma.'),
(24, 'En la firma con id [Identificador de la firma] el certificado firmante se encontraba vencido al momento de realizar la firma según la hora del servidor de estampa de tiempo.'),
(25, 'En la firma con id [Identificador de la firma] se usó un tipo de certificado no válido para realizar la firma.'),
(26, 'En la firma con id [Identificador de la firma] el Target del elemento QualifyingProperties no coincide con el atributo id del tag Signature.'),
(27, 'En la firma con id [Identificador de la firma] el SerialNumber de la sección SignedProperties no coincide con el del certificado firmante.'),
(28, 'En la firma con id [Identificador de la firma] el IssuerName de la sección SignedProperties no coincide con el del certificado firmante.'),
(29, 'En la firma con id [Identificador de la firma] el SerialNumber de la sección KeyInfo no coincide con el del certificado firmante.'),
(30, 'En la firma con id [Identificador de la firma] el IssuerName de la sección KeyInfo no coincide con el del certificado firmante.'),
(31, 'En la firma con id [Identificador de la firma] el resumen hash del elemento DigestValue de la sección SignedProperties, no coincide con el del certificado firmante.'),
(32, 'En la firma con id [Identificador de la firma] el formato de la fecha/hora indicado en el SigningTime, debe estar en el formato UTC.'),
(33, 'En la firma con id [Identificador de la firma] la integridad de la estampa de tiempo de la firma está comprometida.'),
(34, 'En la firma con id [Identificador de la firma] el certificado de la TSA contenido en la primera estampa de tiempo no coincide con el que se encuentra en el elemento CertificateValues.'),
(35, 'En la firma con id [Identificador de la firma] la integridad de la segunda estampa de tiempo está comprometida.'),
(36, 'En la firma con id [Identificador de la firma] el certificado de la TSA contenido en la segunda estampa de tiempo no coincide con el que se encuentra en el elemento CertificateValues.'),
(37, 'En la firma con id [Identificador de la firma] el número de referencias indicadas en el elemento CompleteCertificateRefs, no concuerda con la cantidad de certificados indicado en el elemento de CertificateValues.'),
(38, 'En la firma con id [Identificador de la firma] existe una referencia en el elemento CompleteCertificateRefs, que no coincide con ningún certificado de la sección CertificateValues.'),
(39, ' En la firma con id [Identificador de la firma] el SerialNumber [Serial Number] de la sección CompleteCertificateRefs, no coincide con el SerialNumber [Serial Number] del certificado referenciado de la sección CertificateValues.'),
(40, 'En la firma con id [Identificador de la firma] el IssuerName [Issuer Name] de la sección CompleteCertificateRefs, no coincide con el emisor [Emisor] del certificado referenciado de la sección CertificateValues.'),
(41, 'En la firma con id [Identificador de la firma] el tag ResponderID debe contener al menos un elemento ByKey o un elemento ByName.'),
(42, 'En la firma con id [Identificador de la firma] el valor indicado en el elemento ByKey, no coincide con el hash de la llave pública  del certificado de OCSP.'),
(43, 'En la firma con id [Identificador de la firma] el valor indicado en el elemento ByName, no coincide con el valor del campo CN del Subject del certificado de OCSP.'),
(44, 'En la firma con id [Identificador de la firma] el número de referencias indicadas en el elemento de OcspRefs, no concuerdan con la cantidad de datos de revocación indicados en el elemento OcspValues.'),
(45, 'En la firma con id [Identificador de la firma] existe una referencia en el elemento OCSPRef, que no coincide con ningún dato de revocación de la sección OCSPValues.'),
(46, 'En la firma con id [Identificador de la firma] el valor del elemento ProduceAT, no coincide con el de la respuesta OCSP.'),
(47, 'En la firma con id [Identificador de la firma] el número de referencias indicadas en el elemento de CrlRefs, no concuerdan con la cantidad de datos de revocación indicados en el elemento CrlValues.'),
(48, 'En la firma con id [Identificador de la firma] existe una referencia en el elemento CRLRef, que no coincide con ningún dato de revocación de la sección CRLValues.'),
(49, 'En la firma con id [Identificador de la firma] un elemento Issuer de la sección CRLRef no coincide con el emisor del CRL referenciado en la sección CRLValues.'),
(50, 'En la firma con id [Identificador de la firma] un elemento IssueTime de la sección CRLRef, no coincide con el CRL referenciado en la sección CRLValues.'),
(51, 'En la firma con id [Identificador de la firma] un elemento Number  de la sección CRLRef, no coincide con el CRL referenciado en la sección CRLValues.'),
(52, 'En la firma [Identificador de la firma] no se incluyó la totalidad de los certificados que componen la cadena de la jerarquía nacional de estampa de tiempo.'),
(53, 'En la firma [Identificador de la firma] la jerarquía que emitió el certificado de estampa de tiempo [Cn del sujeto del certificado] no es válida en Costa Rica.'),
(54, 'En la firma con id [Identificador de la firma] no se incluyó la totalidad de los certificados que componen la cadena de la jerarquía nacional del certificado del firmante.'),
(55, 'En la firma con id [Identificador de la firma] la jerarquía que emitió el certificado del firmante [Cn del sujeto del certificado] no es válida en Costa Rica.'),
(56, 'En la firma con id [Identificador de la firma] no se incluyó la totalidad de los certificados que componen la cadena de la jerarquía nacional del certificado de [Cn del sujeto del certificado].'),
(57, 'En la firma con id [Identificador de la firma] la jerarquía que emitió el certificado de [firma, Tsa, Ocsp] [Cn de la raíz que no es validad] no es válida en Costa Rica.'),
(58, 'En la firma con id [Identificador de la firma] se encontraron certificados de más los cuales no son necesarios para la validación de la firma.'),
(59, 'En la firma con id [Identificador de la firma] para el certificado [Cn del sujeto del certificado] no se encontró un CRL para verificar si estaba revocado en el momento de la firma.'),
(60, 'En la firma con id [Identificador de la firma] el certificado [Cn del sujeto del certificado] estaba revocado en el momento de la firma.'),
(61, 'En la firma con id [Identificador de la firma] el certificado [Cn del sujeto del certificado] estaba vencido en el momento de la firma.'),
(62, 'En la firma con id [Identificador de la firma] alguno de los CRLs no se encontraban válidos en el momento de la firma.'),
(63, 'En la firma con id [Identificador de la firma] alguno de los CRLs no fueron emitidos por una CA de la jerarquía nacional.'),
(64, 'En la firma con id [Identificador de la firma] no existen los CRLs necesarios para validar la revocación del certificado firmante. Debe incluirse el CRL Base y el CRL Delta.'),
(65, 'En la firma con id [Identificador de la firma] se encontraron CRLs de más, los cuales no son necesarios para la validación de la revocación.'),
(66, 'En la firma con id [Identificador de la firma] el CRLIndicator del Crl Delta es mayor al CrlNumber del Crl Base.'),
(67, 'El documento no es válido.'),
(68, 'En la firma con id [Identificador de la firma] el certificado contenido en la respuesta OCSP, no coincide con el que se encuentra en el elemento CertificateValues.'),    
)

ERRORES_EN_DOCUMENTO = (
('CrlExtra', 'Crl Extra'),
('IssuerNameNoCoincide', 'Issuer Name No Coincide'),
('CertificadoExtra', 'Certificado Extra'),
('CrlsNoValidos', 'Crls No Validos'),
('EntidadNoSeEncuentraRegistrada', 'Entidad No Se Encuentra Registrada'),
('CrlNoValido', 'Crl No Valido'),
('CertificadosNoValidos', 'Certificados No Validos'),
('HashCertificadoFirmanteNoCoincide', 'Hash Certificado Firmante No Coincide'),
('CompleteCertRefsEmisoresDistintos', 'Complete Cert Refs Emisores Distintos'),
('EstampaDeTiempoDeFirmaIntegridadComprometida', 'Estampa De Tiempo De Firma Integridad Comprometida'),
('DocumentoXmlConEstructuraInvalida', 'Documento Xml Con Estructura Invalida'),
('NumeroDeSerieNoCoincide', 'Numero De Serie No Coincide'),
('DocumentoXmlSinQualifyingProperties', 'Documento Xml Sin Qualifying Properties'),
('CertificadoFirmanteNoValido', 'Certificado Firmante No Valido'),
('CrlDeltaYBaseNoIncluidos', 'Crl Delta Y Base No Incluidos'),
('EntidadSeEncuentraInactiva', 'Entidad Se Encuentra Inactiva'),
('CertificadoDeSegundaEstampaNoCoincide', 'Certificado De Segunda Estampa No Coincide'),
('ResponderIdIncorrecto', 'Responder Id Incorrecto'),
('RespuestaOcspNoValida', 'Respuesta Ocsp No Valida'),
('JerarquiaDeCertificadoHojaIncompleta', 'Jerarquia De Certificado Hoja Incompleta'),
('EstampaDeTiempoDeFirmaNoValida', 'Estampa De Tiempo De Firma No Valida'),
('SignatureValueNoValido', 'Signature Value No Valido'),
('CrlVencido', 'Crl Vencido'),
('NumeroDeCrlIncorrecto', 'Numero De Crl Incorrecto'),
('OcspNoAsociadaACertificado', 'Ocsp No Asociada A Certificado'),
('ProduceAtDeOcspIncorrecto', 'Produce At De Ocsp Incorrecto'),
('ReferenciaAOcspNoValida', 'Referencia A Ocsp No Valida'),
('IssueTimeDeCrlIncorrecto', 'Issue Time De Crl Incorrecto'),
('JerarquiaDeCertificadoFirmanteNoValida', 'Jerarquia De Certificado Firmante No Valida'),
('CertificadoOcspNoCoincide', 'Certificado Ocsp No Coincide'),
('SerialNumberNoCoincide', 'Serial Number No Coincide'),
('SigningTimeFormatoNoValido', 'Signing Time Formato No Valido'),
('SegundaEstampaDeTiempoNoValida', 'Segunda Estampa De Tiempo No Valida'),
('CertificadoVencido', 'Certificado Vencido'),
('IssuerDeCrlIncorrecto', 'Issuer De Crl Incorrecto'),
('ReferenciaACertificadoNoValida', 'Referencia A Certificado No Valida'),
('ProblemasAlValidar', 'Problemas Al Validar'),
('JerarquiaDeCertificadoFirmanteIncompleta', 'Jerarquia De Certificado Firmante Incompleta'),
('CertificadoRevocado', 'Certificado Revocado'),
('TipoDeCertificadoFirmanteNoValido', 'Tipo De Certificado Firmante No Valido'),
('HashReferenciaPropiedadesFirmadasNoCoincide', 'Hash Referencia Propiedades Firmadas No Coincide'),
('SegundaEstampaDeTiempoIntegridadComprometida', 'Segunda Estampa De Tiempo Integridad Comprometida'),
('CertificadoSinCRL', 'Certificado Sin C R L'),
('CantidadDeReferenciasACertificadosIncorrecta', 'Cantidad De Referencias A Certificados Incorrecta'),
('CertificadoFirmanteVencido', 'Certificado Firmante Vencido'),
('CertificadoDeEstampaDeFirmaNoCoincide', 'Certificado De Estampa De Firma No Coincide'),
('CantidadDeReferenciasCrlIncorrecta', 'Cantidad De Referencias Crl Incorrecta'),
('ByNameNoCoincideConLlaveOcsp', 'By Name No Coincide Con Llave Ocsp'),
('CantidadDeReferenciasOcspIncorrecta', 'Cantidad De Referencias Ocsp Incorrecta'),
('SinErrores', 'Sin Errores'),
('ByKeyNoCoincideConLlaveOcsp', 'By Key No Coincide Con Llave Ocsp'),
('CertificadoFirmanteEstadoDesconocido', 'Certificado Firmante Estado Desconocido'),
('QualifyingPropertiesContraIdSignature', 'Qualifying Properties Contra Id Signature'),
('ReferenciaACrlNoValida', 'Referencia A Crl No Valida'),
('JerarquiaDeCertificadoHojaNoValida', 'Jerarquia De Certificado Hoja No Valida'),
('CertificadoFirmanteRevocado', 'Certificado Firmante Revocado'),
('CrlIndicatorNoValido', 'Crl Indicator No Valido'),
('DocumentoXmlInvalido', 'Documento Xml Invalido'),

)

ERRORES_DOCUMENTO_COFIRMA=(
('FirmaSinPrefijo', 'Firma Sin Prefijo'),
('CertificadoTSANoIncluido', 'Certificado T S A No Incluido'),
('ReferenciaSignedPropertiesConTransform', 'Referencia Signed Properties Con Transform'),
('HashReferenciaDocumentoOriginalNoCoincide', 'Hash Referencia Documento Original No Coincide'),
('DataObjectFormatNoValido', 'Data Object Format No Valido'),
('ReferenciaADocumentoOriginalSinTransform', 'Referencia A Documento Original Sin Transform'),
('ReferenciaDocumentoOriginalNoExiste', 'Referencia Documento Original No Existe'),
('ReferenciaDocumentoConType', 'Referencia Documento Con Type'),
('MimeTypeNoPermitido', 'Mime Type No Permitido'),
('ReferenciaAPropiedadesFirmadasSinType', 'Referencia A Propiedades Firmadas Sin Type'),
('ReferenciaPropiesdadesFirmadasNoExiste', 'Referencia Propiesdades Firmadas No Existe'),
('RespuestaOcspFueraDeLasEstampas', 'Respuesta Ocsp Fuera De Las Estampas'),
('DocumentoXmlNoFirmado', 'Documento Xml No Firmado'),
('HashReferenciaKeyInfoNoCoincide', 'Hash Referencia Key Info No Coincide'),
('ReferenciaKeyInfoNoExiste', 'Referencia Key Info No Existe'),
('ReferenciaKeyInfoConTransform', 'Referencia Key Info Con Transform'),
('ReferenciaKeyInfoConType', 'Referencia Key Info Con Type'),
('CantidadDataObjectFormatIncorrecta', 'Cantidad Data Object Format Incorrecta'),
('MimeTypeCadenaNoValida', 'Mime Type Cadena No Valida'),
('CertificadoOcspNoIncluido', 'Certificado Ocsp No Incluido'),
('EncodingNoPermitido', 'Encoding No Permitido'),
('KeyValueNoCoincideConLlavePublica', 'Key Value No Coincide Con Llave Publica'),    
)

ERRORES_DOCUMENTO_CONTRAFIRMA=(
('FirmaSinPrefijo', 'Firma Sin Prefijo'),
('CertificadoTSANoIncluido', 'Certificado T S A No Incluido'),
('ReferenciaSignedPropertiesConTransform', 'Referencia Signed Properties Con Transform'),
('HashReferenciaDocumentoOriginalNoCoincide', 'Hash Referencia Documento Original No Coincide'),
('HashReferenciaCountersignedSignatureNoCoincide', 'Hash Referencia Countersigned Signature No Coincide'),
('DataObjectFormatNoValido', 'Data Object Format No Valido'),
('ReferenciaCountersignedSignatureNoExiste', 'Referencia Countersigned Signature No Existe'),
('ReferenciaADocumentoOriginalSinTransform', 'Referencia A Documento Original Sin Transform'),
('ReferenciaDocumentoOriginalNoExiste', 'Referencia Documento Original No Existe'),
('ReferenciaDocumentoConType', 'Referencia Documento Con Type'),
('ReferenciaACountersignedSignatureSinType', 'Referencia A Countersigned Signature Sin Type'),
('MimeTypeNoPermitido', 'Mime Type No Permitido'),
('ReferenciaAPropiedadesFirmadasSinType', 'Referencia A Propiedades Firmadas Sin Type'),
('ReferenciaPropiesdadesFirmadasNoExiste', 'Referencia Propiesdades Firmadas No Existe'),
('RespuestaOcspFueraDeLasEstampas', 'Respuesta Ocsp Fuera De Las Estampas'),
('DocumentoXmlNoFirmado', 'Documento Xml No Firmado'),
('HashReferenciaKeyInfoNoCoincide', 'Hash Referencia Key Info No Coincide'),
('ReferenciaKeyInfoNoExiste', 'Referencia Key Info No Existe'),
('ReferenciaKeyInfoConTransform', 'Referencia Key Info Con Transform'),
('ReferenciaKeyInfoConType', 'Referencia Key Info Con Type'),
('CantidadDataObjectFormatIncorrecta', 'Cantidad Data Object Format Incorrecta'),
('MimeTypeCadenaNoValida', 'Mime Type Cadena No Valida'),
('CertificadoOcspNoIncluido', 'Certificado Ocsp No Incluido'),
('EncodingNoPermitido', 'Encoding No Permitido'),
('KeyValueNoCoincideConLlavePublica', 'Key Value No Coincide Con Llave Publica'),    
)

ERRORES_DOCUMENTO_MSOFFICE=(
('ReferenciaAManifestConTypeNoValido', 'Referencia A Manifest Con Type No Valido'),
('ReferenciaManifestNoExiste', 'Referencia Manifest No Existe'),
('ReferenciaOfficeObjectSinType', 'Referencia Office Object Sin Type'),
('DocumentoInvalido', 'Documento Invalido'),
('DocumentoNoFirmado', 'Documento No Firmado'),
('ReferenciasDeRelacionEnManifestSinType', 'Referencias De Relacion En Manifest Sin Type'),
('ReferenciaOfficeObjectNoExiste', 'Referencia Office Object No Existe'),
('ReferenciaAPropiedadesFirmadasSinType', 'Referencia A Propiedades Firmadas Sin Type'),
('HashReferenciaManifestNoCoincide', 'Hash Referencia Manifest No Coincide'),
('HashReferenciaDeParteNoCoincide', 'Hash Referencia De Parte No Coincide'),
('ReferenciaConTransformInvalido', 'Referencia Con Transform Invalido'),
('ReferenciaOfficeObjectConTransform', 'Referencia Office Object Con Transform'),
('HashReferenciaNoCoincide', 'Hash Referencia No Coincide'),
('ReferenciaAPropiedadesFirmadasConTypeNoValido', 'Referencia A Propiedades Firmadas Con Type No Valido'),
('ReferenciaEnManifestNoExiste', 'Referencia En Manifest No Existe'),
('JerarquiaDeCertificadoTSANoValida', 'Jerarquia De Certificado T S A No Valida'),
('ReferenciaPropiedadesFirmadasNoExiste', 'Referencia Propiedades Firmadas No Existe'),
('ValorDelSignatureTimeIncorrecto', 'Valor Del Signature Time Incorrecto'),
('ReferenciaAPropiedadesFirmadasSinTransform', 'Referencia A Propiedades Firmadas Sin Transform'),
('HashReferenciaOfficeObjectNoCoincide', 'Hash Referencia Office Object No Coincide'),
('ReferenciaManifestConTransform', 'Referencia Manifest Con Transform'),
('ReferenciaAOfficeObjectConTypeNoValido', 'Referencia A Office Object Con Type No Valido'),
('JerarquiaDeCertificadoTSAIncompleta', 'Jerarquia De Certificado T S A Incompleta'),
('FormatoDelSignatureTimeIncorrecto', 'Formato Del Signature Time Incorrecto'),    
)

ERRORES_DOCUMENTO_ODF=(
('HashReferenciaSignaturePropertiesNoCoincide', 'Hash Referencia Signature Properties No Coincide'),
('keyInfoIssuerNameNoValido', 'key Info Issuer Name No Valido'),
('ReferenciaNoExiste', 'Referencia No Existe'),
('HashReferenciaNoCoincide', 'Hash Referencia No Coincide'),
('ReferenciaAPropiedadesFirmadasConTypeNoValido', 'Referencia A Propiedades Firmadas Con Type No Valido'),
('JerarquiaDeCertificadoTSANoValida', 'Jerarquia De Certificado T S A No Valida'),
('SignaturePropertyTimeFormatoNoValido', 'Signature Property Time Formato No Valido'),
('DocumentoInvalido', 'Documento Invalido'),
('keyInfoSerialNumberNoValido', 'key Info Serial Number No Valido'),
('JerarquiaDeCertificadoTSAIncompleta', 'Jerarquia De Certificado T S A Incompleta'),
('DocumentoNoFirmado', 'Documento No Firmado'),
('ReferenciaPropiedadesFirmadasNoExiste', 'Referencia Propiedades Firmadas No Existe'),    
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

ERRORES_VALIDA_XMLCOFIRMA
--------------------------

=======\t============
Código\tDescripción 
=======\t============
%s
=======\t============

ERRORES_VALIDA_XMLCONTRAFIRMA
------------------------------

=======\t============
Código\tDescripción 
=======\t============
%s
=======\t============

ERRORES_VALIDA_MSOFFICE
--------------------------

=======\t============
Código\tDescripción 
=======\t============
%s
=======\t============

ERRORES_VALIDA_ODF
--------------------------

=======\t============
Código\tDescripción 
=======\t============
%s
=======\t============

ERRORES_EN_DOCUMENTO
----------------------

Estos son códigos generales para todos los tipos de documentos que se pueden 
validar.

===============================================\t============
Código\tDescripción 
===============================================\t============
%s
===============================================\t============

ERRORES_DOCUMENTO_COFIRMA
----------------------------

===============================================\t============
Código\tDescripción 
===============================================\t============
%s
===============================================\t============

ERRORES_DOCUMENTO_CONTRAFIRMA
-------------------------------

===============================================\t============
Código\tDescripción 
===============================================\t============
%s
===============================================\t============

ERRORES_DOCUMENTO_MSOFFICE
-------------------------------

===============================================\t============
Código\tDescripción 
===============================================\t============
%s
===============================================\t============

ERRORES_DOCUMENTO_ODF
-------------------------------

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
           "\n".join(["%s\t%s" % (x, y)
                      for x, y in ERRORES_VALIDAR_XMLCOFIRMA]),
           "\n".join(["%s\t%s" % (x, y)
                      for x, y in ERRORES_VALIDAR_XMLCONTRAFIRMA]),
           "\n".join(["%s\t%s" % (x, y)
                      for x, y in ERRORES_VALIDAR_MSOFFICE]),
           "\n".join(["%s\t%s" % (x, y)
                      for x, y in ERRORES_VALIDAR_ODF]),
           "\n".join(["%s\t%s" % (span_text(x), y)
                      for x, y in ERRORES_EN_DOCUMENTO]),
           "\n".join(["%s\t%s" % (span_text(x), y)
                      for x, y in ERRORES_DOCUMENTO_COFIRMA]),
           "\n".join(["%s\t%s" % (span_text(x), y)
                      for x, y in ERRORES_DOCUMENTO_CONTRAFIRMA]),
           "\n".join(["%s\t%s" % (span_text(x), y)
                      for x, y in ERRORES_DOCUMENTO_MSOFFICE]),
           "\n".join(["%s\t%s" % (span_text(x), y)
                      for x, y in ERRORES_DOCUMENTO_ODF]),           
           )
    return __doc__

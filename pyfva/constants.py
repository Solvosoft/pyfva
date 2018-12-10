'''
Created on 30 jul. 2017

@author: luis
'''
HASH_METHODS = (
    ('Sha256', 'Sha256'),
    ('Sha256', 'Sha256'),
    ('Sha512', 'Sha512'),
)

TIPO_IDENTIFICACION = (
   (1, "Identificación Nacional"),
   (2, "DIMEX"), 
   (3, "DIDI")    
)

ENTIDAD_NO_REGISTRADA = 4

ERRORES_AL_SOLICITAR_FIRMA = (
(0, "Solicitud recibida correctamente."),
(1, "Ha ocurrido algún problema al solicitar la firma o autenticación."),
(2, "Solicitud con campos incompletos."),
(3, "Existe una diferencia no permitida entre la fecha y hora del cliente y la del servidor. La fecha/hora de la solicitud no debe tener una diferencia de más de 60 segundos de la fecha/hora del servidor."),
(ENTIDAD_NO_REGISTRADA, "La entidad no se encuentra registrada."),
(5, "La entidad se encuentra en estado inactiva."),
(6, "El negocio no pertenece a la entidad solicitante."),
(7, "El tamaño del resumen de la solicitud de firma es no valido, este debe ser mayor a 1 y menor a  250 caracteres."),
(8, "El tamaño de la razón de firma de la solicitud de firma PAdES es inválida, este debe ser mayor a 1 y menor a  125 caracteres."),
(9, "El suscriptor se encuentra desconectado para recibir una solicitud."),
(10, "El formato de la identificación enviado no es válido, este debe tener un formato para un nacional 0#-####-#### para un DIDI 5########### para un DIMEX 1###########")

)

ERRORES_AL_NOTIFICAR_FIRMA = (
    (0, "Solicitud completada sin errores."),
    (1, "Ha ocurrido algún problema al firmar."),
    (2, "Solicitud de firma rechazada por el suscriptor."),
    (3, "El suscriptor ha excedido el tiempo máximo permitido para firmar la solicitud."),
    (4, "El suscriptor se encuentra desconectado para recibir una solicitud de firma."),
    (5, "El documento XML de la solicitud contiene una marca de bytes (BOM) no permitido."),
    (6, "El documento de la solicitud es inválido."),
    (7, "Error no definido en el estandar"),
    (8, "El hash de la solicitud es incorrecto."),
    (9, "El certificado del suscriptor está revocado."),
    (10, "El certificado del suscriptor está vencido."),
    (11, "Existe una solicitud de firma en proceso para el cliente."),
    (12, "No se pudo notificar a la entidad."),
    (13, "El código de verificación es incorrecto"),
    (14, "El suscriptor bloqueo el pin de la tarjeta"),
    (15, "El documento no es válido para ser contrafirmado.")
)

ERRORES_VALIDA_CERTIFICADO = (
    (0, 'Certificado válido.'),
    (1, 'Error interno al validar el certificado.'),
    (2, 'Los bytes enviados no corresponden a  un certificado.'),
    (3, 'El certificado del suscriptor está vencido.'),
    (4, 'El certificado del suscriptor está revocado.'),
    (5, 'El Certificado enviado no es de confianza porque no es emitido  por la CA Raíz Nacional.'),
    (6, 'El certificado enviado no es de autenticación.'),
    (7, 'El certificado tiene un problema de estructura, no cuenta con el oid  de ocsp en el que se encuentra la dirección del servicio.'),
    (8, 'El certificado tiene un problema de estructura, no cuenta con los usos de la clave necesarios para un certificado de autenticación.'),
    (9, 'El certificado tiene un problema de estructura, el campo  CN del sujeto tiene una estructura inválida.'),
    (10, 'El certificado tiene un problema de estructura, el campo  SERIALNUMBER del sujeto tiene una estructura inválida.'),
    (11, 'La entidad no se encuentra registrada.'),
    (12, 'La entidad no se encuentra en estado inactiva.')
)

ERRORES_VALIDAR_XMLCOFIRMA=(
(0, "Documento válido."), 
(1, "Error interno al validar el documento."), 
(2, "La entidad no se encuentra registrada."), 
(3, "La entidad se encuentra en estado inactiva."), 
(4, "El documento no es un XML válido."), 
(5, "El documento XML no se encuentra firmado."), 
(6, "La firma con id [Identificador de la firma] no contiene el tag QualifyingProperties o no se ha definido el prefijo Etsi [http://uri.etsi.org/01903/v1.3.2#]."), 
(7, "La firma con id [Identificador de la firma] contiene una estructura no valida."), 
(8, "La firma con id [Identificador de la firma] contiene un certificado firmante con un formato no válido."), 
(9, "La firma con id [Identificador de la firma] contiene [Cantidad de certificados] certificados con un formato no válido."), 
(10, "La firma con id [Identificador de la firma] contiene una respuesta OCSP no válida."), 
(11, "La estampa de tiempo de la firma con id [Identificador de la firma] no es válida."), 
(12, "La segunda estampa de la firma con id [Identificador de la firma] tiempo no es válida."), 
(13, "La firma con id [Identificador de la firma] contiene [Cantidad de  CRL's] certificados CRL's con un formato no válido."), 
(14, "No se encontró la referencia que apunta al elemento KeyInfo en la firma con id [Identificador de la firma]."), 
(15, "No se encontró la referencia que apunta al elemento SignedProperties en la firma con id [Identificador de la firma]."), 
(16, "No se encontró la referencia que apunta al documento original en la firma con id [Identificador de la firma]."), 
(17, "La firma con id [Identificador de la firma] no contiene el tag Transform en la referencia al documento original."), 
(18, "La firma con id [Identificador de la firma] no cuenta con el atributo Type en la referencia a las propiedades firmadas."), 
(19, "El atributo Type no debe estar dentro de la referencia que apunta al documento original en la firma con id [Identificador de la firma]."), 
(20, "El atributo Type no debe estar dentro de la referencia que apunta a la sección KeyInfo en la firma con id [Identificador de la firma]."), 
(21, "El elemento Transform no debe estar dentro de la referencia que apunta a SignedProperties en la firma con id [Identificador de la firma]."), 
(22, "El elemento Transform no debe estar dentro de la referencia que apunta a la sección KeyInfo en la firma con id [Identificador de la firma]."), 
(23, "En la firma con id [Identificador de la firma] el DigestValue de la referencia relacionada con el elemento KeyInfo no coincide."), 
(24, "En la firma con id [Identificador de la firma] el DigestValue de la referencia relacionada con el elemento SignedProperties no coincide."), 
(25, "En la firma con id [Identificador de la firma] el DigestValue de la referencia relacionada con el documento original no coincide."), 
(26, "En la firma con id [Identificador de la firma] el valor de la firma en el tag SignatureValue,  no coincide con los elementos firmados del elemento SignedInfo,  puede ser que la integridad del documento haya sido comprometida."), 
(27, "En la firma con id [Identificador de la firma] los valores indicados en el elemento KeyValue no coinciden con la llave pública del certificado."), 
(28, "En la firma con id [Identificador de la firma] la respuesta OCSP del documento no coincide con el certificado firmante."), 
(29, "En la firma con id [Identificador de la firma] el certificado firmante se encontraba revocado al momento de realizar la firma."), 
(30, "En la firma con id [Identificador de la firma] el certificado firmante tenía un formato no válido al momento de realizar la firma."), 
(31, "En la firma con id [Identificador de la firma] el certificado firmante se encontraba vencido al momento de realizar la firma según la hora del servidor de estampa de tiempo. "), 
(32, "En la firma con id [Identificador de la firma] se usó un tipo de certificado no válido para realizar la firma."), 
(33, "En la firma con id [Identificador de la firma] el Target del elemento QualifyingProperties no coincide con el atributo id del tag Signature."), 
(34, "En la firma con id [Identificador de la firma] el SerialNumber de la sección SignedProperties no coincide con el del certificado firmante. "), 
(35, "En la firma con id [Identificador de la firma] el IssuerName de la sección SignedProperties no coincide con el del certificado firmante."), 
(36, "En la firma con id [Identificador de la firma] algún elemento MimeType no está dentro de los permitidos."), 
(37, "En la firma con id [Identificador de la firma] el MimeType utilizado sobrepasa la longitud máxima de caracteres (90 caracteres)."), 
(38, "En la firma con id [Identificador de la firma] algún encoding no está dentro de los permitidos."), 
(39, "En la firma con id [Identificador de la firma] la cantidad de DataObjectFormat es incorrecta."), 
(40, "En la firma con id [Identificador de la firma] algún elemento DataObjectFormat referencia a un elemento no válido en la sección SignedInfo."), 
(41, "En la firma con id [Identificador de la firma] el resumen hash del elemento DigestValue de la sección SignedProperties,  no coincide con el del certificado firmante."), 
(42, "En la firma con id [Identificador de la firma] el formato de la fecha/hora indicado en el SigningTime,  debe estar en el formato UTC."), 
(43, "En la firma con id [Identificador de la firma] la integridad de la estampa de tiempo de la firma está comprometida."), 
(44, "En la firma con id [Identificador de la firma] el certificado de la TSA contenido en la primera estampa de tiempo no coincide con el que se encuentra en el elemento CertificateValues."), 
(45, "En la firma con id [Identificador de la firma] la integridad de la segunda estampa de tiempo está comprometida."), 
(46, "En la firma con id [Identificador de la firma] el certificado de la TSA contenido en la segunda estampa de tiempo no coincide con el que se encuentra en el elemento CertificateValues."), 
(47, "En la firma con id [Identificador de la firma] el número de referencias indicadas en el elemento CompleteCertificateRefs,  no concuerda con la cantidad de certificados indicado en el elemento de CertificateValues."), 
(48, "En la firma con id [Identificador de la firma] existe una referencia en el elemento CompleteCertificateRefs,  que no coincide con ningún certificado de la sección CertificateValues."), 
(49, "En la firma con id [Identificador de la firma] el SerialNumber [Serial Number] de la sección CompleteCertificateRefs,  no coincide con el SerialNumber [Serial Number] del certificado referenciado de la sección CertificateValues."), 
(50, "En la firma con id [Identificador de la firma] el IssuerName  [Nombre del emisor] de la sección CompleteCertificateRefs,  no coincide con el emisor [Nombre del emisor] del certificado referenciado de la sección CertificateValues."), 
(51, "En la firma con id [Identificador de la firma] el tag ResponderID debe contener al menos un elemento ByKey o un elemento ByName."), 
(52, "En la firma con id [Identificador de la firma] el valor indicado en el elemento ByKey,  no coincide con el hash de la llave pública  del certificado de OCSP."), 
(53, "En la firma con id [Identificador de la firma] el valor indicado en el elemento ByName,  no coincide con el valor del campo CN del Subject del certificado de OCSP."), 
(54, "En la firma con id [Identificador de la firma] el número de referencias indicadas en el elemento de OcspRefs,  no concuerdan con la cantidad de datos de revocación indicados en el elemento OcspValues."), 
(55, "En la firma con id [Identificador de la firma] existe una referencia en el elemento OCSPRef,  que no coincide con ningún dato de revocación de la sección OCSPValues."), 
(56, "En la firma con id [Identificador de la firma] el valor del elemento ProduceAT,  no coincide con el de la respuesta OCSP."), 
(57, "En la firma con id [Identificador de la firma] el número de referencias indicadas en el elemento de CrlRefs,  no concuerdan con la cantidad de datos de revocación indicados en el elemento CrlValues."), 
(58, "En la firma con id [Identificador de la firma] existe una referencia en el elemento CRLRef,  que no coincide con ningún dato de revocación de la sección CRLValues."), 
(59, "En la firma con id [Identificador de la firma] un elemento Issuer de la sección CRLRef no coincide con el emisor del CRL referenciado en la sección CRLValues"), 
(60, "En la firma con id [Identificador de la firma] un elemento IssueTime de la sección CRLRef,  no coincide con el CRL referenciado en la sección CRLValues."), 
(61, "En la firma con id [Identificador de la firma] un elemento Number  de la sección CRLRef,  no coincide con el CRL referenciado en la sección CRLValues."), 
(62, "En la firma con id [Identificador de la firma] no se incluyó la totalidad de los certificados que componen la cadena de la jerarquía nacional del certificado del firmante."), 
(63, "En la firma con id [Identificador de la firma] la jerarquía que emitió el certificado del firmante [Cn del sujeto del certificado raíz] no es válida en Costa Rica."), 
(64, "En la firma con id [Identificador de la firma] no se incluyó la totalidad de los certificados que componen la cadena de la jerarquía nacional del certificado de [firma,  Tsa,  Ocsp]."), 
(65, "En la firma con id [Identificador de la firma] la jerarquía que emitió el certificado de [firma,  Tsa,  Ocsp] [Cn de la raíz que no es validad] no es válida en Costa Rica."), 
(66, "En la firma con id [Identificador de la firma] no se encontró  el certificado de TSA necesario para validar la firma."), 
(67, "En la firma con id [Identificador de la firma] no se encontró el certificado de OCSP necesario para validar la firma."), 
(68, "En la firma con id [Identificador de la firma] se encontraron certificados de más los cuales no son necesarios para la validación de la firma."), 
(69, "En la firma con id [Identificador de la firma] para el certificado [Cn del sujeto del certificado] no se encontró un CRL para verificar si estaba revocado en el momento de la firma."), 
(70, "En la firma con id [Identificador de la firma] el certificado  certificado [Cn del sujeto del certificado] estaba revocado en el momento de la firma."), 
(71, "En la firma con id [Identificador de la firma] el certificado  certificado [Cn del sujeto del certificado] estaba vencido en el momento de la firma."), 
(72, "En la firma con id [Identificador de la firma] el certificado contenido en la respuesta OCSP,  no coincide con el que se encuentra en el elemento CertificateValues."), 
(73, "En la firma con id [Identificador de la firma] la respuesta OCSP no se encontraba válida en el momento de la firma."), 
(74, "En la firma con id [Identificador de la firma] alguno de los CRLs no se encontraban válidos en el momento de la firma."), 
(75, "En la firma con id [Identificador de la firma] alguno de los CRLs no fueron emitidos por una CA de la jerarquía nacional."), 
(76, "En la firma con id [Identificador de la firma] se encontraron CRLs de más,  los cuales no son necesarios para la validación de la revocación."), 
(77, "En la firma con id [Identificador de la firma] el CRLIndicator del Crl Delta es mayor el CrlNumber del Crl Base."), 
(78, "Para la firma con id [Identificador de la firma] no se ha definido el prefijo DS [http://www.w3.org/2000/09/xmldsig#]."), 
(79, "En la firma con id [Identificador de la firma] para el certificado firmante [Sujeto] no se encontró una respuesta OCSP o los CRLs necesarios para validar el estado de revocación."), 
(80, "En la firma [Identificador de la firma] no se incluyó el CRL [Delta,  Base],  el cual es necesario para verificar el estado de revocación del certificado firmante de [Sujeto].")
)

ERRORES_VALIDAR_XMLCONTRAFIRMA=(
(0, "Documento válido."), 
(1, "Error interno al validar el documento."), 
(2, "La entidad no se encuentra registrada."), 
(3, "La entidad se encuentra en estado inactiva."), 
(4, "El documento no es un XML válido."), 
(5, "El documento XML no se encuentra firmado."), 
(6, "La firma con id [Identificador de la firma] no contiene el tag QualifyingProperties o no se ha definido el prefijo Etsi [http://uri.etsi.org/01903/v1.3.2#]."), 
(7, "La firma con id [Identificador de la firma] contiene una estructura no valida."), 
(8, "La firma con id [Identificador de la firma] contiene un certificado firmante con un formato no válido."), 
(9, "La firma con id [Identificador de la firma] contiene [Cantidad de certificados] certificados con un formato no válido."), 
(10, "La firma con id [Identificador de la firma] contiene una respuesta OCSP no válida."), 
(11, "La estampa de tiempo de la firma con id [Identificador de la firma] no es válida."), 
(12, "La segunda estampa de la firma con id [Identificador de la firma] tiempo no es válida."), 
(13, "La firma con id [Identificador de la firma] contiene [Cantidad de  CRL's] certificados CRL's con un formato no válido."), 
(14, "No se encontró la referencia que apunta al elemento KeyInfo en la firma con id [Identificador de la firma]."), 
(15, "No se encontró la referencia que apunta al elemento SignedProperties en la firma con id [Identificador de la firma]."), 
(16, "No se encontró la referencia que apunta al documento original en la firma con id [Identificador de la firma]."), 
(17, "La firma con id [Identificador de la firma] no contiene el tag Transform en la referencia al documento original."), 
(18, "La firma con id [Identificador de la firma] no cuenta con el atributo Type en la referencia a las propiedades firmadas."), 
(19, "El atributo Type no debe estar dentro de la referencia que apunta al documento original en la firma con id [Identificador de la firma]."), 
(20, "El atributo Type no debe estar dentro de la referencia que apunta a la sección KeyInfo en la firma con id [Identificador de la firma]."), 
(21, "El elemento Transform no debe estar dentro de la referencia que apunta a SignedProperties en la firma con id [Identificador de la firma]."), 
(22, "El elemento Transform no debe estar dentro de la referencia que apunta a la sección KeyInfo en la firma con id [Identificador de la firma]."), 
(23, "En la firma con id [Identificador de la firma] el DigestValue de la referencia relacionada con el elemento KeyInfo no coincide."), 
(24, "En la firma con id [Identificador de la firma] el DigestValue de la referencia relacionada con el elemento SignedProperties no coincide."), 
(25, "En la firma con id [Identificador de la firma] el DigestValue de la referencia relacionada con el documento original no coincide."), 
(26, "En la firma con id [Identificador de la firma] el valor de la firma en el tag SignatureValue,  no coincide con los elementos firmados del elemento SignedInfo,  puede ser que la integridad del documento haya sido comprometida."), 
(27, "En la firma con id [Identificador de la firma] los valores indicados en el elemento KeyValue no coinciden con la llave pública del certificado."), 
(28, "En la firma con id [Identificador de la firma] la respuesta OCSP del documento no coincide con el certificado firmante."), 
(29, "En la firma con id [Identificador de la firma] el certificado firmante se encontraba revocado al momento de realizar la firma."), 
(30, "En la firma con id [Identificador de la firma] el certificado firmante tenía un formato no válido al momento de realizar la firma."), 
(31, "En la firma con id [Identificador de la firma] el certificado firmante se encontraba vencido al momento de realizar la firma según la hora del servidor de estampa de tiempo. "), 
(32, "En la firma con id [Identificador de la firma] se usó un tipo de certificado no válido para realizar la firma."), 
(33, "En la firma con id [Identificador de la firma] el Target del elemento QualifyingProperties no coincide con el atributo id del tag Signature."), 
(34, "En la firma con id [Identificador de la firma] el SerialNumber de la sección SignedProperties no coincide con el del certificado firmante. "), 
(35, "En la firma con id [Identificador de la firma] el IssuerName de la sección SignedProperties no coincide con el del certificado firmante."), 
(36, "En la firma con id [Identificador de la firma] algún elemento MimeType no está dentro de los permitidos."), 
(37, "En la firma con id [Identificador de la firma] el MimeType utilizado sobrepasa la longitud máxima de caracteres (90 caracteres)."), 
(38, "En la firma con id [Identificador de la firma] algún encoding no está dentro de los permitidos."), 
(39, "En la firma con id [Identificador de la firma] la cantidad de DataObjectFormat es incorrecta."), 
(40, "En la firma con id [Identificador de la firma] algún elemento DataObjectFormat referencia a un elemento no válido en la sección SignedInfo."), 
(41, "En la firma con id [Identificador de la firma] el resumen hash del elemento DigestValue de la sección SignedProperties,  no coincide con el del certificado firmante."), 
(42, "En la firma con id [Identificador de la firma] el formato de la fecha/hora indicado en el SigningTime,  debe estar en el formato UTC."), 
(43, "En la firma con id [Identificador de la firma] la integridad de la estampa de tiempo de la firma está comprometida."), 
(44, "En la firma con id [Identificador de la firma] el certificado de la TSA contenido en la primera estampa de tiempo no coincide con el que se encuentra en el elemento CertificateValues."), 
(45, "En la firma con id [Identificador de la firma] la integridad de la segunda estampa de tiempo está comprometida."), 
(46, "En la firma con id [Identificador de la firma] el certificado de la TSA contenido en la segunda estampa de tiempo no coincide con el que se encuentra en el elemento CertificateValues."), 
(47, "En la firma con id [Identificador de la firma] el número de referencias indicadas en el elemento CompleteCertificateRefs,  no concuerda con la cantidad de certificados indicado en el elemento de CertificateValues."), 
(48, "En la firma con id [Identificador de la firma] existe una referencia en el elemento CompleteCertificateRefs,  que no coincide con ningún certificado de la sección CertificateValues."), 
(49, "En la firma con id [Identificador de la firma] el SerialNumber [Serial Number] de la sección CompleteCertificateRefs,  no coincide con el SerialNumber [Serial Number] del certificado referenciado de la sección CertificateValues."), 
(50, "En la firma con id [Identificador de la firma] el IssuerName  [Nombre del emisor] de la sección CompleteCertificateRefs,  no coincide con el emisor [Nombre del emisor] del certificado referenciado de la sección CertificateValues."), 
(51, "En la firma con id [Identificador de la firma] el tag ResponderID debe contener al menos un elemento ByKey o un elemento ByName."), 
(52, "En la firma con id [Identificador de la firma] el valor indicado en el elemento ByKey,  no coincide con el hash de la llave pública  del certificado de OCSP."), 
(53, "En la firma con id [Identificador de la firma] el valor indicado en el elemento ByName,  no coincide con el valor del campo CN del Subject del certificado de OCSP."), 
(54, "En la firma con id [Identificador de la firma] el número de referencias indicadas en el elemento de OcspRefs,  no concuerdan con la cantidad de datos de revocación indicados en el elemento OcspValues."), 
(55, "En la firma con id [Identificador de la firma] existe una referencia en el elemento OCSPRef,  que no coincide con ningún dato de revocación de la sección OCSPValues."), 
(56, "En la firma con id [Identificador de la firma] el valor del elemento ProduceAT,  no coincide con el de la respuesta OCSP."), 
(57, "En la firma con id [Identificador de la firma] el número de referencias indicadas en el elemento de CrlRefs,  no concuerdan con la cantidad de datos de revocación indicados en el elemento CrlValues."), 
(58, "En la firma con id [Identificador de la firma] existe una referencia en el elemento CRLRef,  que no coincide con ningún dato de revocación de la sección CRLValues."), 
(59, "En la firma con id [Identificador de la firma] un elemento Issuer de la sección CRLRef no coincide con el emisor del CRL referenciado en la sección CRLValues"), 
(60, "En la firma con id [Identificador de la firma] un elemento IssueTime de la sección CRLRef,  no coincide con el CRL referenciado en la sección CRLValues."), 
(61, "En la firma con id [Identificador de la firma] un elemento Number  de la sección CRLRef,  no coincide con el CRL referenciado en la sección CRLValues."), 
(62, "En la firma con id [Identificador de la firma] no se incluyó la totalidad de los certificados que componen la cadena de la jerarquía nacional del certificado del firmante."), 
(63, "En la firma con id [Identificador de la firma] la jerarquía que emitió el certificado del firmante [Cn del sujeto del certificado raíz] no es válida en Costa Rica."), 
(64, "En la firma con id [Identificador de la firma] no se incluyó la totalidad de los certificados que componen la cadena de la jerarquía nacional del certificado de [firma,  Tsa,  Ocsp]."), 
(65, "En la firma con id [Identificador de la firma] la jerarquía que emitió el certificado de [firma,  Tsa,  Ocsp] [Cn de la raíz que no es validad] no es válida en Costa Rica."), 
(66, "En la firma con id [Identificador de la firma] no se encontró  el certificado de TSA necesario para validar la firma."), 
(67, "En la firma con id [Identificador de la firma] no se encontró el certificado de OCSP necesario para validar la firma."), 
(68, "En la firma con id [Identificador de la firma] se encontraron certificados de más los cuales no son necesarios para la validación de la firma."), 
(69, "En la firma con id [Identificador de la firma] para el certificado [Cn del sujeto del certificado] no se encontró un CRL para verificar si estaba revocado en el momento de la firma."), 
(70, "En la firma con id [Identificador de la firma] el certificado  certificado [Cn del sujeto del certificado] estaba revocado en el momento de la firma."), 
(71, "En la firma con id [Identificador de la firma] el certificado  certificado [Cn del sujeto del certificado] estaba vencido en el momento de la firma."), 
(72, "En la firma con id [Identificador de la firma] el certificado contenido en la respuesta OCSP,  no coincide con el que se encuentra en el elemento CertificateValues."), 
(73, "En la firma con id [Identificador de la firma] la respuesta OCSP no se encontraba válida en el momento de la firma."), 
(74, "En la firma con id [Identificador de la firma] alguno de los CRLs no se encontraban válidos en el momento de la firma."), 
(75, "En la firma con id [Identificador de la firma] alguno de los CRLs no fueron emitidos por una CA de la jerarquía nacional."), 
(76, "En la firma con id [Identificador de la firma] se encontraron CRLs de más,  los cuales no son necesarios para la validación de la revocación."), 
(77, "En la firma con id [Identificador de la firma] el CRLIndicator del Crl Delta es mayor el CrlNumber del Crl Base."), 
(78, "Para la firma con id [Identificador de la firma] no se ha definido el prefijo DS [http://www.w3.org/2000/09/xmldsig#]."), 
(79, "No se encontró la referencia que apunta al elemento SignatureValue en la Contra Firma con id [Identificador de la firma]."), 
(80, "La firma con el id [Identificador de la firma] no cuenta con el atributo Type en la referencia al SignatureValue de la firma anterior."), 
(81, "En la firma con id [Identificador de la firma] el DigestValue de la referencia al SignatureValue de la firma anterior no coincide."), 
(82, "En la firma con id [Identificador de la firma] para el certificado firmante [Sujeto] no se encontró una respuesta OCSP o los CRLs necesarios para validar el estado de revocación."), 
(83, "En la firma [Identificador de la firma] no se incluyó el CRL [Delta,  Base],  el cual es necesario para verificar el estado de revocación del certificado firmante de [Sujeto].")
)


ERRORES_VALIDAR_MSOFFICE=(
(0, "Documento válido. "), 
(1, "Error interno al validar el documento. "), 
(2, "La entidad enviada no se encuentra registrada. "), 
(3, "La entidad enviada se encuentra en estado Inactiva."), 
(4, "El documento no es un XML válido"), 
(5, "El documento no se encuentra firmado"), 
(6, "La firma [Identificador de la firma] no contiene el tag QualifyingProperties o no se ha definido el prefijo Etsi [http://uri.etsi.org/01903/v1.3.2#]."), 
(7, "La firma [Identificador de la firma] contiene una estructura no valida."), 
(8, "La firma [Identificador de la firma] contiene un certificado firmante con un formato no válido."), 
(9, "La firma [Identificador de la firma] contiene [Cantidad de certificados] certificados con un formato no válido."), 
(10, "La firma [Identificador de la firma] contiene una respuesta OCSP no válida."), 
(11, "La estampa de tiempo de la firma [Identificador de la firma] no es válida."), 
(12, "La segunda estampa de tiempo de la firma [Identificador de la firma] no es válida."), 
(13, "La firma [Identificador de la firma] contiene [Cantidad de  CRL's] CRL's con un formato no válido."), 
(14, "No se encontró la referencia que apunta al elemento Manifest en la firma [Identificador de la firma]."), 
(15, "La firma [Identificador de la firma] no cuenta con el atributo Type en la referencia de relación."), 
(16, "No se encontró la referencia que apunta al elemento SignedProperties en la firma [Identificador de la firma].  "), 
(17, "No se encontró la referencia del documento [La URI de la referencia] en la firma [Identificador de la firma]."), 
(18, "La firma [Identificador de la firma] no cuenta con el atributo Type en la referencia a las propiedades firmadas. "), 
(19, "La firma [Identificador de la firma] cuenta un atributo Type inválido en la referencia a las propiedades firmadas."), 
(20, "La firma [Identificador de la firma] no cuenta con un atributo Transform en la referencia a las propiedades firmadas invalido."), 
(21, "El elemento Transform no debe estar dentro de la referencia que apunta a la sección KeyInfo en la firma [Identificador de la firma]."), 
(22, "El elemento Transform no debe estar dentro de la referencia que apunta a la sección Manifest en la firma [Identificador de la firma]."), 
(23, "En la firma [Identificador de la firma] las propiedades firmadas tienen un algoritmo de transformación no válido."), 
(24, "En la firma [Identificador de la firma] el DigestValue de la referencia relacionada con el elemento SignedProperties no coincide."), 
(25, "En la firma [Identificador de la firma] el DigestValue de la referencia relacionada con el elemento Manifest no coincide."), 
(26, "En la firma [Identificador de la firma] el DigestValue de la referencia relacionada con el elemento OfficeObject no coincide."), 
(27, "En la firma [Identificador de la firma] el DigestValue de la referencia de parte del documento [Uri] en el elemento Manifest no coincide."), 
(28, "En la firma [Identificador de la firma] el DigestValue de la referencia del documento [URI] en el elemento Manifest no coincide."), 
(29, "En la firma [Identificador de la firma] el valor de la firma en el tag SignatureValue,  no coincide con los elementos firmados del elemento SignedInfo,  puede ser que la integridad del documento haya sido comprometida."), 
(30, "En la firma [Identificador de la firma] la respuesta OCSP del documento no coincide con el certificado firmante."), 
(31, "En la firma [Identificador de la firma] el certificado firmante se encontraba revocado al momento de realizar la firma."), 
(32, "En la firma [Identificador de la firma] el certificado firmante tenía un formato no válido al momento de realizar la firma."), 
(33, "En la firma [Identificador de la firma] el certificado firmante se encontraba vencido al momento de realizar la firma según la hora del servidor de estampa de tiempo."), 
(34, "En la firma [Identificador de la firma] se usó un tipo de certificado no válido para realizar la firma"), 
(35, "En la firma [Identificador de la firma] el Target del elemento QualifyingProperties no coincide con el atributo id del tag Signature."), 
(36, "En la firma con [Identificador de la firma] el SerialNumber de la sección SignedProperties no coincide con el del certificado firmante."), 
(37, "En la firma con [Identificador de la firma] el IssuerName de la sección SignedProperties no coincide con el del certificado firmante."), 
(38, "En la firma [Identificador de la firma] el resumen hash del elemento DigestValue de la sección SignedProperties,  no coincide con el del certificado firmante."), 
(39, "En la firma [Identificador de la firma] el formato de la fecha/hora indicado en el SigningTime,  debe estar en el formato UTC."), 
(40, "En la firma [Identificador de la firma] la integridad de la estampa de tiempo de la firma está comprometida."), 
(41, "En la firma [Identificador de la firma] el certificado de la TSA contenido en la primera estampa de tiempo no coincide con el que se encuentra en el elemento CertificateValues."), 
(42, "En la firma [Identificador de la firma] la integridad de la segunda estampa de tiempo está comprometida."), 
(43, "En la firma [Identificador de la firma] el certificado de la TSA contenido en la segunda estampa de tiempo no coincide con el que se encuentra en el elemento CertificateValues."), 
(44, "En la firma [Identificador de la firma] el número de referencias indicadas en el elemento CompleteCertificateRefs,  no concuerda con la cantidad de certificados indicado en el elemento de CertificateValues."), 
(45, "En la firma [Identificador de la firma] existe una referencia en el elemento CompleteCertificateRefs,  que no coincide con ningún certificado de la sección CertificateValues."), 
(46, "En la firma [Identificador de la firma] el SerialNumber [Serial Number] de la sección CompleteCertificateRefs,  no coincide con el SerialNumber [Serial Number] del certificado referenciado de la sección CertificateValues."), 
(47, "En la firma [Identificador de la firma] el IssuerName [Issuer Name] de la sección CompleteCertificateRefs,  no coincide con el emisor [Emisor] del certificado referenciado de la sección CertificateValues."), 
(48, "En la firma [Identificador de la firma] el tag ResponderID debe contener al menos un elemento ByKey o un elemento ByName."), 
(49, "En la firma [Identificador de la firma] el valor indicado en el elemento ByKey,  no coincide con el hash de la llave pública  del certificado de OCSP."), 
(50, "En la firma [Identificador de la firma] el valor indicado en el elemento ByName,  no coincide con el valor del campo CN del Subject del certificado de OCSP."), 
(51, "En la firma [Identificador de la firma] el número de referencias indicadas en el elemento de OcspRefs,  no concuerdan con la cantidad de datos de revocación indicados en el elemento OcspValues."), 
(52, "En la firma [Identificador de la firma] existe una referencia en el elemento OCSPRef,  que no coincide con ningún dato de revocación de la sección OCSPValues."), 
(53, "En la firma [Identificador de la firma] el valor del elemento ProduceAT,  no coincide con el de la respuesta OCSP."), 
(54, "En la firma [Identificador de la firma] el número de referencias indicadas en el elemento de CrlRefs,  no concuerdan con la cantidad de datos de revocación indicados en el elemento CrlValues."), 
(55, "En la firma [Identificador de la firma] existe una referencia en el elemento CRLRef,  que no coincide con ningún dato de revocación de la sección CRLValues."), 
(56, "En la firma [Identificador de la firma] un elemento Issuer de la sección CRLRef no coincide con el emisor del CRL referenciado en la sección CRLValues"), 
(57, "En la firma [Identificador de la firma] un elemento IssueTime de la sección CRLRef,  no coincide con el CRL referenciado en la sección CRLValues."), 
(58, "En la firma [Identificador de la firma] un elemento Number  de la sección CRLRef,  no coincide con el CRL referenciado en la sección CRLValues."), 
(59, "En la firma [Identificador de la firma] no se incluyó la totalidad de los certificados que componen la cadena de la jerarquía nacional del certificado del firmante."), 
(60, "En la firma [Identificador de la firma] la jerarquía que emitió el certificado del firmante no es válida en Costa Rica."), 
(61, "En la firma [Identificador de la firma] no se incluyó la totalidad de los certificados que componen la cadena de la jerarquía nacional de estampa de tiempo."), 
(62, "En la firma [Identificador de la firma] la jerarquía que emitió el certificado de estampa de tiempo [Tsa] no es válida en Costa Rica."), 
(63, "En la firma [Identificador de la firma] no se incluyó la totalidad de los certificados que componen la cadena de la jerarquía nacional del certificado de [Cn del sujeto del certificado]."), 
(64, "En la firma [Identificador de la firma] la jerarquía que emitió el certificado de [firma,  Tsa,  Ocsp] [Cn de la raíz que no es validad] no es válida en Costa Rica."), 
(65, "En la firma [Identificador de la firma] se encontraron certificados de más,  los cuales no son necesarios para la validación de la firma."), 
(66, "En la firma [Identificador de la firma] para el certificado [Cn del sujeto del certificado] no se encontró un CRL para verificar si estaba revocado en el momento de la firma."), 
(67, "En la firma [Identificador de la firma] el certificado [Cn del sujeto del certificado] estaba revocado en el momento de la firma."), 
(68, "En la firma [Identificador de la firma] el certificado [Cn del sujeto del certificado] estaba vencido en el momento de la firma."), 
(69, "En la firma [Identificador de la firma] el certificado contenido en la respuesta OCSP,  no coincide con el que se encuentra en el elemento CertificateValues."), 
(70, "En la firma [Identificador de la firma] alguno de los CRLs no se encontraban válidos en el momento de la firma."), 
(71, "En la firma [Identificador de la firma] alguno de los CRLs no fueron emitidos por una CA de la jerarquía nacional."), 
(72, "En la firma [Identificador de la firma] se encontraron CRLs de más,  los cuales no son necesarios para la validación de la revocación."), 
(73, "En la firma [Identificador de la firma]  el CRLIndicator del Crl Delta es mayor al CrlNumber del Crl Base."), 
(74, "El documento no es válido."), 
(75, "En la firma [Identificador de la firma] el formato del SignatureTime es incorrecto."), 
(76, "En la firma [Identificador de la firma] el formato del valor de la fecha del SignatureTime es incorrecto."), 
(77, "La firma [Identificador de la firma] no cuenta con el atributo Type en la referencia al Office Object"), 
(78, "La firma [Identificador de la firma] no cuenta con un atributo Type valido en la referencia a Office Object."), 
(79, "La firma [Identificador de la firma] no cuenta con un atributo Type valido en la referencia de relación."), 
(80, "No se encontró la referencia que apunta al elemento Office Object en la firma [Identificador de la firma]."), 
(81, "En la firma con id [Identificador de la firma] para el certificado firmante [Sujeto] no se encontró una respuesta OCSP o los CRLs necesarios para validar el estado de revocación."), 
(82, "En la firma [Identificador de la firma] no se incluyó el CRL [Base,  Delta],  el cual es necesario para verificar el estado de revocación del certificado firmante de [Sujeto del Certificado]."), 
(83, "En la firma [Identificador de la firma] la respuesta OCSP no se encontraba válida en el momento de la firma.")
)


ERRORES_VALIDAR_ODF=(
(0, "Documento válido. "), 
(1, "Error interno al validar el documento. "), 
(2, "La entidad enviada no se encuentra registrada. "), 
(3, "La entidad enviada se encuentra en estado Inactiva."), 
(4, "El documento no es un XML válido"), 
(5, "El documento no se encuentra firmado"), 
(6, "La firma [Identificador de la firma] no contiene el tag QualifyingProperties o no se ha definido el prefijo Etsi [http://uri.etsi.org/01903/v1.3.2#]."), 
(7, "La firma con id [Identificador de la firma] contiene una estructura no valida."), 
(8, "La firma con id [Identificador de la firma] contiene un certificado firmante con un formato no válido."), 
(9, "La firma con id [Identificador de la firma] contiene [Cantidad de certificados]  certificados con un formato no válido."), 
(10, "La firma con id [Identificador de la firma] contiene una respuesta OCSP no válida."), 
(11, "La estampa de tiempo de la firma con id [Identificador de la firma] no es válida."), 
(12, "La segunda estampa de tiempo de la firma con id [Identificador de la firma] no es válida."), 
(13, "La firma con id [Identificador de la firma] contiene [Cantidad de certificados]  CRL's con un formato no válido."), 
(14, "No se encontró la referencia en la firma con id [Identificador de la firma]."), 
(15, "En la firma con id [Identificador de la firma] el DigestValue de la referencia no coincide."), 
(16, "La firma [Identificador de la firma] cuenta con un atributo Type no válido en la referencia a las propiedades firmadas."), 
(17, "No se encontró la referencia que apunta al elemento SignedProperties en la firma con id [Identificador de la firma]. "), 
(18, "En la firma con id [Identificador de la firma] el DigestValue de la referencia relacionada con el elemento SignatureProperties no coincide."), 
(19, "En la firma con id [Identificador de la firma] el DigestValue de la referencia relacionada con el elemento SignedProperties no coincide."), 
(20, "En la firma con id [Identificador de la firma] el valor de la firma en el tag SignatureValue,  no coincide con los elementos firmados del elemento SignedInfo,  puede ser que la integridad del documento haya sido comprometida."), 
(21, "En la firma con id [Identificador de la firma] la respuesta OCSP del documento no coincide con el certificado firmante."), 
(22, "En la firma con id [Identificador de la firma] el certificado firmante se encontraba revocado al momento de realizar la firma."), 
(23, "En la firma con id [Identificador de la firma] el certificado firmante tenía un formato no válido al momento de realizar la firma."), 
(24, "En la firma con id [Identificador de la firma] el certificado firmante se encontraba vencido al momento de realizar la firma según la hora del servidor de estampa de tiempo."), 
(25, "En la firma con id [Identificador de la firma] se usó un tipo de certificado no válido para realizar la firma."), 
(26, "En la firma con id [Identificador de la firma] el Target del elemento QualifyingProperties no coincide con el atributo id del tag Signature."), 
(27, "En la firma con id [Identificador de la firma] el SerialNumber de la sección SignedProperties no coincide con el del certificado firmante."), 
(28, "En la firma con id [Identificador de la firma] el IssuerName de la sección SignedProperties no coincide con el del certificado firmante."), 
(29, "En la firma con id [Identificador de la firma] el SerialNumber de la sección KeyInfo no coincide con el del certificado firmante."), 
(30, "En la firma con id [Identificador de la firma] el IssuerName de la sección KeyInfo no coincide con el del certificado firmante."), 
(31, "En la firma con id [Identificador de la firma] el resumen hash del elemento DigestValue de la sección SignedProperties,  no coincide con el del certificado firmante."), 
(32, "En la firma con id [Identificador de la firma] el formato de la fecha/hora indicado en el SigningTime,  debe estar en el formato UTC."), 
(33, "En la firma con id [Identificador de la firma] la integridad de la estampa de tiempo de la firma está comprometida."), 
(34, "En la firma con id [Identificador de la firma] el certificado de la TSA contenido en la primera estampa de tiempo no coincide con el que se encuentra en el elemento CertificateValues."), 
(35, "En la firma con id [Identificador de la firma] la integridad de la segunda estampa de tiempo está comprometida."), 
(36, "En la firma con id [Identificador de la firma] el certificado de la TSA contenido en la segunda estampa de tiempo no coincide con el que se encuentra en el elemento CertificateValues."), 
(37, "En la firma con id [Identificador de la firma] el número de referencias indicadas en el elemento CompleteCertificateRefs,  no concuerda con la cantidad de certificados indicado en el elemento de CertificateValues."), 
(38, "En la firma con id [Identificador de la firma] existe una referencia en el elemento CompleteCertificateRefs,  que no coincide con ningún certificado de la sección CertificateValues."), 
(39, " En la firma con id [Identificador de la firma] el SerialNumber [Serial Number] de la sección CompleteCertificateRefs,  no coincide con el SerialNumber [Serial Number] del certificado referenciado de la sección CertificateValues."), 
(40, "En la firma con id [Identificador de la firma] el IssuerName [Issuer Name] de la sección CompleteCertificateRefs,  no coincide con el emisor [Emisor] del certificado referenciado de la sección CertificateValues."), 
(41, "En la firma con id [Identificador de la firma] el tag ResponderID debe contener al menos un elemento ByKey o un elemento ByName."), 
(42, "En la firma con id [Identificador de la firma] el valor indicado en el elemento ByKey,  no coincide con el hash de la llave pública  del certificado de OCSP."), 
(43, "En la firma con id [Identificador de la firma] el valor indicado en el elemento ByName,  no coincide con el valor del campo CN del Subject del certificado de OCSP."), 
(44, "En la firma con id [Identificador de la firma] el número de referencias indicadas en el elemento de OcspRefs,  no concuerdan con la cantidad de datos de revocación indicados en el elemento OcspValues."), 
(45, "En la firma con id [Identificador de la firma] existe una referencia en el elemento OCSPRef,  que no coincide con ningún dato de revocación de la sección OCSPValues."), 
(46, "En la firma con id [Identificador de la firma] el valor del elemento ProduceAT,  no coincide con el de la respuesta OCSP."), 
(47, "En la firma con id [Identificador de la firma] el número de referencias indicadas en el elemento de CrlRefs,  no concuerdan con la cantidad de datos de revocación indicados en el elemento CrlValues."), 
(48, "En la firma con id [Identificador de la firma] existe una referencia en el elemento CRLRef,  que no coincide con ningún dato de revocación de la sección CRLValues."), 
(49, "En la firma con id [Identificador de la firma] un elemento Issuer de la sección CRLRef no coincide con el emisor del CRL referenciado en la sección CRLValues."), 
(50, "En la firma con id [Identificador de la firma] un elemento IssueTime de la sección CRLRef,  no coincide con el CRL referenciado en la sección CRLValues."), 
(51, "En la firma con id [Identificador de la firma] un elemento Number  de la sección CRLRef,  no coincide con el CRL referenciado en la sección CRLValues."), 
(52, "En la firma [Identificador de la firma] no se incluyó la totalidad de los certificados que componen la cadena de la jerarquía nacional de estampa de tiempo."), 
(53, "En la firma [Identificador de la firma] la jerarquía que emitió el certificado de estampa de tiempo [Cn del sujeto del certificado] no es válida en Costa Rica."), 
(54, "En la firma con id [Identificador de la firma] no se incluyó la totalidad de los certificados que componen la cadena de la jerarquía nacional del certificado del firmante."), 
(55, "En la firma con id [Identificador de la firma] la jerarquía que emitió el certificado del firmante [Cn del sujeto del certificado] no es válida en Costa Rica."), 
(56, "En la firma con id [Identificador de la firma] no se incluyó la totalidad de los certificados que componen la cadena de la jerarquía nacional del certificado de [Cn del sujeto del certificado]."), 
(57, "En la firma con id [Identificador de la firma] la jerarquía que emitió el certificado de [firma,  Tsa,  Ocsp] [Cn de la raíz que no es validad] no es válida en Costa Rica."), 
(58, "En la firma con id [Identificador de la firma] se encontraron certificados de más los cuales no son necesarios para la validación de la firma."), 
(59, "En la firma con id [Identificador de la firma] para el certificado [Cn del sujeto del certificado] no se encontró un CRL para verificar si estaba revocado en el momento de la firma."), 
(60, "En la firma con id [Identificador de la firma] el certificado [Cn del sujeto del certificado] estaba revocado en el momento de la firma."), 
(61, "En la firma con id [Identificador de la firma] el certificado [Cn del sujeto del certificado] estaba vencido en el momento de la firma."), 
(62, "En la firma con id [Identificador de la firma] alguno de los CRLs no se encontraban válidos en el momento de la firma."), 
(63, "En la firma con id [Identificador de la firma] alguno de los CRLs no fueron emitidos por una CA de la jerarquía nacional."), 
(64, "En la firma con id [Identificador de la firma] se encontraron CRLs de más,  los cuales no son necesarios para la validación de la revocación."), 
(65, "En la firma con id [Identificador de la firma] el CRLIndicator del Crl Delta es mayor al CrlNumber del Crl Base."), 
(66, "El documento no es válido."), 
(67, "En la firma con id [Identificador de la firma] el certificado contenido en la respuesta OCSP,  no coincide con el que se encuentra en el elemento CertificateValues."), 
(68, "En la firma con id [Identificador de la firma] el formato de la fecha/hora indicado en el SignatureProperty,  debe estar en el formato 'yyyy-MM-dd'T'HH:mm:ss.fffffff00'."), 
(69, "En la firma con id [Identificador de la firma] para el certificado firmante [Sujeto del Certificado] no se encontró una respuesta OCSP o los CRLs necesarios para validar el estado de revocación."), 
(70, "En la firma [Identificador de la firma] no se incluyó el CRL (Base,  Delta),  el cual es necesario para verificar el estado de revocación del certificado firmante de [Sujeto del Certificado]."), 
(71, "En la firma [Identificador de la firma] la respuesta OCSP no se encontraba válida en el momento de la firma.")
)

ERRORES_VALIDAR_PDF=(
(0, "Documento válido."),
(1, "Error interno al validar el documento."),
(2, "La entidad no se encuentra registrada."),
(3, "La entidad enviada se encuentra en estado Inactiva."),
(4, "El documento no es un PDF válido."),
(5, "El documento PDF no se encuentra firmado."),
(6, "El documento firmado no contiene un DSS (Document Security Store)."),
(7, "La última firma no corresponde a una firma de estampado de tiempo de documento (Document Time-Stamp)."),
(8, "La secuencia de las firmas no es correcta."),
(9, "En el documento firmado el DSS (Document Security Store) contiene [Cantidad de certificados]   certificados con un formato no válido."),
(10, "En el documento firmado el DSS (Document Security Store) contiene [Cantidad de certificados]  respuestas OCSP con un formato no válido."),
(11, "En el documento firmado el DSS (Document Security Store) contiene [Cantidad de certificados]  CRLs con un formato no válido."),
(12, "La última firma de estampado de tiempo no cubre todo el documento."),
(13, "La integridad de la firma [Identificador de la firma] está comprometida."),
(14, "En la firma [Identificador de la firma] la integridad de la estampa de tiempo de la firma está comprometida."),
(15, "En la firma [Identificador de la firma] la estampa de tiempo no se firmó con el certificado contenido."),
(16, "La firma [Identificador de la firma] no contiene la estampa de tiempo."),
(17, "El DSS (Document Security Store) no contiene la información necesaria para la validar la firma [Identificador de la firma]."),
(18, "En la firma [Identificador de la firma] se encontraron certificados de más los cuales no son necesarios para la validación de la firma."),
(19, "En la firma [Identificador de la firma] el certificado firmante tenía un formato no válido al momento de realizar la firma."),
(20, "En la firma [Identificador de la firma] el certificado firmante se encontraba revocado al momento de realizar la firma."),
(21, "En la firma [Identificador de la firma] no se incluyó la totalidad de los certificados que componen la cadena de la jerarquía nacional del certificado de [Cn del sujeto del certificado]."),
(22, "En la firma [Identificador de la firma] la jerarquía que emitió el certificado de [Cn del sujeto del certificado] ({[Tipo del Certificado]}) no es válida en Costa Rica."),
(23, "En la firma [Identificador de la firma] el certificado [Cn del sujeto del certificado] estaba revocado en el momento de la firma."),
(24, "En la firma [Identificador de la firma] para el certificado [Cn del sujeto del certificado]  no se encontró un CRL para verificar si estaba revocado en el momento de la firma."),
(25, "En la firma [Identificador de la firma] el certificado [Cn del sujeto del certificado]  estaba vencido en el momento de la firma."),
(26, "En la firma [Identificador de la firma] se usó un tipo de certificado no válido para realizar la firma."),
(27, "En la firma [Identificador de la firma] el CRL emitido por [Cn del emisor del certificado]   no se encontraba válido en el momento de la firma."),
(28, "En la firma [Identificador de la firma] el CRL emitido por [Cn del emisor del certificado] no fue emitido por una CA de la jerarquía nacional."),
(29, "En la firma [Identificador de la firma] no se incluyó el CRL [Base o Delta], el cual es necesario para verificar el estado de revocación del certificado firmante de [Cn del sujeto del certificado]."),
(30, "En la firma [Identificador de la firma] se encontraron CRLs de más, los cuales no son necesarios para la validación de la revocación."),
(31, "En la firma [Identificador de la firma] el CRLIndicator del CRL Delta es mayor al CrlNumber del Crl Base."),
(32, "Para la última firma [Identificador de la firma] no fue posible obtener la cadena en línea del certificado de TSA."),
(33, "Para la última firma [Identificador de la firma] no fue posible obtener los CRLs en línea del certificado de TSA."),
(34, "Para la última firma [Identificador de la firma] el CRL obtenido en línea y emitido por [Cn del emisor del certificado] se encuentra vencido."),
(35, "Para la última firma [Identificador de la firma] el CRL obtenido en línea y emitido por [Cn del emisor del certificado] no fue emitido por una CA de la jerarquía nacional."),
(36, "Para la última firma [Identificador de la firma] no fue posible obtener la totalidad de los certificados que componen la cadena de la jerarquía nacional del certificado de [Cn del sujeto del certificado]."),
(37, "Para la última firma [Identificador de la firma] la jerarquía que emitió el certificado obtenido en línea de [Cn del emisor del certificado] ({[Tipo del Certificado]}) no es válida en Costa Rica."),
(38, "Para la última firma [Identificador de la firma] el certificado [Cn del sujeto del certificado] obtenido en línea está revocado."),
(39, "Para la última firma [Identificador de la firma] no fue posible obtener en línea el CRL del certificado [Cn del sujeto del certificado], para verificar si esta revocado."),
(40, "Para la última firma [Identificador de la firma] el certificado [Cn del sujeto del certificado]  obtenido en línea está vencido."),
(41, "En la firma [Identificador de la firma] para el certificado firmante [Cn del sujeto del certificado] no se encontró una respuesta OCSP o los CRLs necesarios para validar el estado de revocación."),
(42, "En la firma [Identificador de la firma] la respuesta OCSP no se encontraba válida en el momento de la firma."),
(43, "En la firma [Identificador de la firma] la respuesta OCSP no se firmó con el certificado contenido."),
(44, "En la firma [Identificador de la firma] se encontraron respuestas OCSP de más, los cuales no son necesarios para la validación de la revocación."),
(45, "En la firma [Identificador de la firma] se encontraron respuestas OCSP, los cuales no son necesarios para la validación de la revocación."),
(46, "En la firma [Identificador de la firma] no se encontró el certificado de OCSP necesario para validar la firma."),
(47, "En la firma [Identificador de la firma] la respuesta OCSP del documento no coincide con el certificado firmante."),
(48, "La estampa de tiempo que cubre el documento tiene un algoritmo {0} que se considera como inseguro.")
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

ERRORES_VALIDA_PDF
--------------------------

=======\t============
Código\tDescripción 
=======\t============
%s
=======\t============

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
           "\n".join(["%s\t%s" % (x, y)
                      for x, y in ERRORES_VALIDAR_PDF])       
           )
    return __doc__

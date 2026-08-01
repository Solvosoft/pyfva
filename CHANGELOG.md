## 0.0.46

Se agrega soporte completo para firmar, sellar y validar documentos JSON (`json_cofirma`/`json_fhir`),
validado contra las especificaciones oficiales del BCCR (WSDL de `SelladorElectronicoConControlDeLlave`,
WSDL de `ValidadorDeDocumentos` y el OpenAPI de `Firmador`):

* REST: `RestFirmador.firme_json()`/`firme(formato='json_cofirma'|'json_fhir')` usando los servicios
  `firma_json_cofirma`/`firma_json_fhir` ya declarados en `REST_SERVICE_URLS`.
* SOAP Firmador: `ClienteFirmador.firme_json()`/`firme(formato='json_cofirma'|'json_fhir')` agrega las
  operaciones `RecibaLaSolicitudDeFirmaJsonEnvelopingCoFirma`/`...JsonParaArchivosFHIR`.
* SOAP Sello: `ClienteSellador.firme_json()` agrega las operaciones
  `RecibaLaSolicitudDeSelladoElectronicoJsonEnvelopingCoFirma`/`...JsonParaArchivosFHIR`.
* SOAP Validación: `ClienteValidador.validar_documento(formato='json_cofirma'|'json_fhir')` agrega
  las operaciones `ValideElDocumentoJsonEnvelopingCoFirma`/`...JsonParaArchivosFHIR`.
* Se completa la constante `ERRORES_VALIDAR_JSON` reusando el catálogo de `ERRORES_VALIDAR_XMLCOFIRMA`
  (mismo catálogo de errores que documentos XML enveloping cofirma).

Se promueve `pyfva.clientes.validador`/`pyfva.soap.validador_documento` (antes "V2",
`ValidadorDeDocumentos.asmx`) a ubicación canónica sin sufijo, y se elimina la versión V1 obsoleta
(`ValidadorDeDocumento.asmx`, WSDL distinto). `pyfva.clientes.validadorv2` y
`pyfva.soap.validador_documento_v2` se mantienen como alias de compatibilidad hacia atrás.

Se actualiza la dependencia `soapfish2` a la versión `0.7.3` y se integra como dependencia principal (ya no como extra opcional `soap`).

## 1.0.0

Actualización de las versiones soportadas de python 3.11, 3.12, 3.13. Aunque puede funcionar bien en otras versiones.
Incorporación de API Rest de Gaudi.
Se movió el archivo de settings al módulo conf.
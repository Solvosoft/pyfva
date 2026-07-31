'''
Alias de compatibilidad hacia atrás.

`pyfva.soap.validador_documento` es ahora el módulo canónico (antes "V2");
este módulo se mantiene para que el código existente que importa
`validador_documento_v2` siga funcionando sin cambios.
'''

from pyfva.soap.validador_documento import *  # noqa: F401,F403
from pyfva.soap.validador_documento import (  # noqa: F401
    ValideElServicio,
    ValideElServicioResponse,
    ValidadorDeDocumentosSoapServiceStub,
    ValidadorDeDocumentosSoap12ServiceStub,
    ValideElDocumentoXmlEnvelopedCoFirma,
    ValideElDocumentoXmlEnvelopedCoFirmaResponse,
    ValideElDocumentoXmlEnvelopedContraFirma,
    ValideElDocumentoXmlEnvelopedContraFirmaResponse,
    ValideElDocumentoMSOffice,
    ValideElDocumentoMSOfficeResponse,
    ValideElDocumentoOdf,
    ValideElDocumentoOdfResponse,
    ValideElDocumentoPdf,
    ValideElDocumentoPdfResponse,
    ValideElDocumentoJsonEnvelopingCoFirma,
    ValideElDocumentoJsonEnvelopingCoFirmaResponse,
    ValideElDocumentoJsonParaArchivosFHIR,
    ValideElDocumentoJsonParaArchivosFHIRResponse,
    ResultadoValidacion,
)

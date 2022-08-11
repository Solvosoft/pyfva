# flake8:noqa
# isort:skip_file
##############################################################################
# Note: Generated by soapfish.wsdl2py at 2022-05-26 21:10:09.297989+00:00
#       Try to avoid editing it if you might need to regenerate it.
##############################################################################

from soapfish import soap, xsd
from pyfva.soap import settings
BaseHeader = xsd.ComplexType

##############################################################################
# Schemas


# http://bccr.fva.cr/


class AlgoritmoDeHash(xsd.String):
    enumeration = ['Sha256', 'Sha384', 'Sha512']


class SolicitudDeFirma(xsd.ComplexType):
    INHERITANCE = None
    INDICATOR = xsd.Sequence
    Documento = xsd.Element(xsd.Base64Binary, minOccurs=0)
    FechaDeReferenciaDeLaEntidad = xsd.Element(xsd.DateTime, minOccurs=1)
    HashDocumento = xsd.Element(xsd.Base64Binary, minOccurs=0)
    IDAlgoritmoHash = xsd.Element(AlgoritmoDeHash, minOccurs=1)
    CodNegocio = xsd.Element(xsd.Int, minOccurs=1)
    IdFuncionalidad = xsd.Element(xsd.Int, minOccurs=1)

    @classmethod
    def create(cls, FechaDeReferenciaDeLaEntidad, IDAlgoritmoHash, CodNegocio, IdFuncionalidad):
        instance = cls()
        instance.FechaDeReferenciaDeLaEntidad = FechaDeReferenciaDeLaEntidad
        instance.IDAlgoritmoHash = IDAlgoritmoHash
        instance.CodNegocio = CodNegocio
        instance.IdFuncionalidad = IdFuncionalidad
        return instance


class RespuestaDeLaSolicitud(xsd.ComplexType):
    INHERITANCE = None
    INDICATOR = xsd.Sequence
    DocumentoFirmado = xsd.Element(xsd.Base64Binary, minOccurs=0)
    FueExitosa = xsd.Element(xsd.Boolean, minOccurs=1)
    CodigoDeError = xsd.Element(xsd.Int, minOccurs=1)
    HashDocumentoFirmado = xsd.Element(xsd.Base64Binary, minOccurs=0)
    IDAlgoritmoHashDocumentoFirmado = xsd.Element(xsd.Int, minOccurs=1)

    @classmethod
    def create(cls, FueExitosa, CodigoDeError, IDAlgoritmoHashDocumentoFirmado):
        instance = cls()
        instance.FueExitosa = FueExitosa
        instance.CodigoDeError = CodigoDeError
        instance.IDAlgoritmoHashDocumentoFirmado = IDAlgoritmoHashDocumentoFirmado
        return instance


class SolicitudDeFirmaPdf(SolicitudDeFirma):
    INHERITANCE = xsd.Inheritance.EXTENSION
    INDICATOR = xsd.Sequence
    Razon = xsd.Element(xsd.String, minOccurs=0)
    Lugar = xsd.Element(xsd.String, minOccurs=0)

    @classmethod
    def create(cls, CodNegocio, FechaDeReferenciaDeLaEntidad, IDAlgoritmoHash,  IdFuncionalidad):
        instance = cls()
        instance.FechaDeReferenciaDeLaEntidad = FechaDeReferenciaDeLaEntidad
        instance.IDAlgoritmoHash = IDAlgoritmoHash
        instance.CodNegocio = CodNegocio
        instance.IdFuncionalidad = IdFuncionalidad
        return instance


class RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma(xsd.ComplexType):
    INHERITANCE = None
    INDICATOR = xsd.Sequence
    laSolicitud = xsd.Element(SolicitudDeFirma, minOccurs=0)

    @classmethod
    def create(cls):
        instance = cls()
        return instance


class RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirmaResponse(xsd.ComplexType):
    INHERITANCE = None
    INDICATOR = xsd.Sequence
    RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirmaResult = xsd.Element(RespuestaDeLaSolicitud, minOccurs=0)

    @classmethod
    def create(cls):
        instance = cls()
        return instance


class RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma(xsd.ComplexType):
    INHERITANCE = None
    INDICATOR = xsd.Sequence
    laSolicitud = xsd.Element(SolicitudDeFirma, minOccurs=0)

    @classmethod
    def create(cls):
        instance = cls()
        return instance


class RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirmaResponse(xsd.ComplexType):
    INHERITANCE = None
    INDICATOR = xsd.Sequence
    RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirmaResult = xsd.Element(RespuestaDeLaSolicitud, minOccurs=0)

    @classmethod
    def create(cls):
        instance = cls()
        return instance


class RecibaLaSolicitudDeSelladoElectronicoMSOffice(xsd.ComplexType):
    INHERITANCE = None
    INDICATOR = xsd.Sequence
    laSolicitud = xsd.Element(SolicitudDeFirma, minOccurs=0)

    @classmethod
    def create(cls):
        instance = cls()
        return instance


class RecibaLaSolicitudDeSelladoElectronicoMSOfficeResponse(xsd.ComplexType):
    INHERITANCE = None
    INDICATOR = xsd.Sequence
    RecibaLaSolicitudDeSelladoElectronicoMSOfficeResult = xsd.Element(RespuestaDeLaSolicitud, minOccurs=0)

    @classmethod
    def create(cls):
        instance = cls()
        return instance


class RecibaLaSolicitudDeSelladoElectronicoPdf(xsd.ComplexType):
    INHERITANCE = None
    INDICATOR = xsd.Sequence
    laSolicitud = xsd.Element(SolicitudDeFirmaPdf, minOccurs=0)

    @classmethod
    def create(cls):
        instance = cls()
        return instance


class RecibaLaSolicitudDeSelladoElectronicoPdfResponse(xsd.ComplexType):
    INHERITANCE = None
    INDICATOR = xsd.Sequence
    RecibaLaSolicitudDeSelladoElectronicoPdfResult = xsd.Element(RespuestaDeLaSolicitud, minOccurs=0)

    @classmethod
    def create(cls):
        instance = cls()
        return instance


class RecibaLaSolicitudDeSelladoElectronicoOdf(xsd.ComplexType):
    INHERITANCE = None
    INDICATOR = xsd.Sequence
    laSolicitud = xsd.Element(SolicitudDeFirma, minOccurs=0)

    @classmethod
    def create(cls):
        instance = cls()
        return instance


class RecibaLaSolicitudDeSelladoElectronicoOdfResponse(xsd.ComplexType):
    INHERITANCE = None
    INDICATOR = xsd.Sequence
    RecibaLaSolicitudDeSelladoElectronicoOdfResult = xsd.Element(RespuestaDeLaSolicitud, minOccurs=0)

    @classmethod
    def create(cls):
        instance = cls()
        return instance


class ValideElServicio(xsd.ComplexType):
    pass


class ValideElServicioResponse(xsd.ComplexType):
    INHERITANCE = None
    INDICATOR = xsd.Sequence
    ValideElServicioResult = xsd.Element(xsd.Boolean, minOccurs=1)

    @classmethod
    def create(cls, ValideElServicioResult):
        instance = cls()
        instance.ValideElServicioResult = ValideElServicioResult
        return instance


Schema_c49e7 = xsd.Schema(
    imports=[],
    includes=[],
    targetNamespace=settings.FVA_HOST,
    elementFormDefault='qualified',
    simpleTypes=[AlgoritmoDeHash],
    attributeGroups=[],
    groups=[],
    complexTypes=[SolicitudDeFirma, RespuestaDeLaSolicitud, SolicitudDeFirmaPdf],
    elements={'RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma': xsd.Element(RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma()), 'RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirmaResponse': xsd.Element(RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirmaResponse()), 'RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma': xsd.Element(RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma()), 'RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirmaResponse': xsd.Element(RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirmaResponse()), 'RecibaLaSolicitudDeSelladoElectronicoMSOffice': xsd.Element(RecibaLaSolicitudDeSelladoElectronicoMSOffice()), 'RecibaLaSolicitudDeSelladoElectronicoMSOfficeResponse': xsd.Element(RecibaLaSolicitudDeSelladoElectronicoMSOfficeResponse()), 'RecibaLaSolicitudDeSelladoElectronicoPdf': xsd.Element(RecibaLaSolicitudDeSelladoElectronicoPdf()), 'RecibaLaSolicitudDeSelladoElectronicoPdfResponse': xsd.Element(RecibaLaSolicitudDeSelladoElectronicoPdfResponse()), 'RecibaLaSolicitudDeSelladoElectronicoOdf': xsd.Element(RecibaLaSolicitudDeSelladoElectronicoOdf()), 'RecibaLaSolicitudDeSelladoElectronicoOdfResponse': xsd.Element(RecibaLaSolicitudDeSelladoElectronicoOdfResponse()), 'ValideElServicio': xsd.Element(ValideElServicio()), 'ValideElServicioResponse': xsd.Element(ValideElServicioResponse())},
)


##############################################################################
# Methods


RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma_method = xsd.Method(
    soapAction=settings.FVA_HOST + 'RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma',
    input='RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma',
    inputPartName='parameters',
    output='RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirmaResponse',
    outputPartName='parameters',
    operationName='RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma',
    style='document',
)


RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma_method = xsd.Method(
    soapAction=settings.FVA_HOST + 'RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma',
    input='RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma',
    inputPartName='parameters',
    output='RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirmaResponse',
    outputPartName='parameters',
    operationName='RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma',
    style='document',
)


RecibaLaSolicitudDeSelladoElectronicoMSOffice_method = xsd.Method(
    soapAction=settings.FVA_HOST + 'RecibaLaSolicitudDeSelladoElectronicoMSOffice',
    input='RecibaLaSolicitudDeSelladoElectronicoMSOffice',
    inputPartName='parameters',
    output='RecibaLaSolicitudDeSelladoElectronicoMSOfficeResponse',
    outputPartName='parameters',
    operationName='RecibaLaSolicitudDeSelladoElectronicoMSOffice',
    style='document',
)


RecibaLaSolicitudDeSelladoElectronicoPdf_method = xsd.Method(
    soapAction=settings.FVA_HOST + 'RecibaLaSolicitudDeSelladoElectronicoPdf',
    input='RecibaLaSolicitudDeSelladoElectronicoPdf',
    inputPartName='parameters',
    output='RecibaLaSolicitudDeSelladoElectronicoPdfResponse',
    outputPartName='parameters',
    operationName='RecibaLaSolicitudDeSelladoElectronicoPdf',
    style='document',
)


RecibaLaSolicitudDeSelladoElectronicoOdf_method = xsd.Method(
    soapAction=settings.FVA_HOST + 'RecibaLaSolicitudDeSelladoElectronicoOdf',
    input='RecibaLaSolicitudDeSelladoElectronicoOdf',
    inputPartName='parameters',
    output='RecibaLaSolicitudDeSelladoElectronicoOdfResponse',
    outputPartName='parameters',
    operationName='RecibaLaSolicitudDeSelladoElectronicoOdf',
    style='document',
)


ValideElServicio_method = xsd.Method(
    soapAction=settings.FVA_HOST + 'ValideElServicio',
    input='ValideElServicio',
    inputPartName='parameters',
    output='ValideElServicioResponse',
    outputPartName='parameters',
    operationName='ValideElServicio',
    style='document',
)


##############################################################################
# SOAP Service


SelladorElectronicoConControlDeLlaveSoap_SERVICE = soap.Service(
    name='SelladorElectronicoConControlDeLlaveSoap',
    targetNamespace=settings.FVA_HOST,
    location='${scheme}://${host}/'+settings.SERVICE_URLS['sello'],
    schemas=[Schema_c49e7],
    version=soap.SOAPVersion.SOAP12,
    methods=[RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma_method, RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma_method, RecibaLaSolicitudDeSelladoElectronicoMSOffice_method, RecibaLaSolicitudDeSelladoElectronicoPdf_method, RecibaLaSolicitudDeSelladoElectronicoOdf_method, ValideElServicio_method],
)


##############################################################################
# SOAP Service Stub

class SSLContex:
    REQUESTS_CERT_PATH = settings.SELLADOR_CERT_PATH
    REQUESTS_KEY_PATH = settings.SELLADOR_KEY_PATH


class SelladorElectronicoConControlDeLlaveSoapServiceStub(soap.Stub, SSLContex):
    SERVICE = SelladorElectronicoConControlDeLlaveSoap_SERVICE
    SCHEME = settings.STUB_SCHEME
    HOST = settings.STUB_HOST

    def RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma(self, RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma, header=None):
        return self.call('RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma', RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma, header=header)

    def RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma(self, RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma, header=None):
        return self.call('RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma', RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma, header=header)

    def RecibaLaSolicitudDeSelladoElectronicoMSOffice(self, RecibaLaSolicitudDeSelladoElectronicoMSOffice, header=None):
        return self.call('RecibaLaSolicitudDeSelladoElectronicoMSOffice', RecibaLaSolicitudDeSelladoElectronicoMSOffice, header=header)

    def RecibaLaSolicitudDeSelladoElectronicoPdf(self, RecibaLaSolicitudDeSelladoElectronicoPdf, header=None):
        return self.call('RecibaLaSolicitudDeSelladoElectronicoPdf', RecibaLaSolicitudDeSelladoElectronicoPdf, header=header)

    def RecibaLaSolicitudDeSelladoElectronicoOdf(self, RecibaLaSolicitudDeSelladoElectronicoOdf, header=None):
        return self.call('RecibaLaSolicitudDeSelladoElectronicoOdf', RecibaLaSolicitudDeSelladoElectronicoOdf, header=header)

    def ValideElServicio(self, ValideElServicio, header=None):
        return self.call('ValideElServicio', ValideElServicio, header=header)

##############################################################################
# Methods


RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma_method = xsd.Method(
    soapAction=settings.FVA_HOST + 'RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma',
    input='RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma',
    inputPartName='parameters',
    output='RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirmaResponse',
    outputPartName='parameters',
    operationName='RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma',
    style='document',
)


RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma_method = xsd.Method(
    soapAction=settings.FVA_HOST + 'RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma',
    input='RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma',
    inputPartName='parameters',
    output='RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirmaResponse',
    outputPartName='parameters',
    operationName='RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma',
    style='document',
)


RecibaLaSolicitudDeSelladoElectronicoMSOffice_method = xsd.Method(
    soapAction=settings.FVA_HOST + 'RecibaLaSolicitudDeSelladoElectronicoMSOffice',
    input='RecibaLaSolicitudDeSelladoElectronicoMSOffice',
    inputPartName='parameters',
    output='RecibaLaSolicitudDeSelladoElectronicoMSOfficeResponse',
    outputPartName='parameters',
    operationName='RecibaLaSolicitudDeSelladoElectronicoMSOffice',
    style='document',
)


RecibaLaSolicitudDeSelladoElectronicoPdf_method = xsd.Method(
    soapAction=settings.FVA_HOST + 'RecibaLaSolicitudDeSelladoElectronicoPdf',
    input='RecibaLaSolicitudDeSelladoElectronicoPdf',
    inputPartName='parameters',
    output='RecibaLaSolicitudDeSelladoElectronicoPdfResponse',
    outputPartName='parameters',
    operationName='RecibaLaSolicitudDeSelladoElectronicoPdf',
    style='document',
)


RecibaLaSolicitudDeSelladoElectronicoOdf_method = xsd.Method(
    soapAction=settings.FVA_HOST + 'RecibaLaSolicitudDeSelladoElectronicoOdf',
    input='RecibaLaSolicitudDeSelladoElectronicoOdf',
    inputPartName='parameters',
    output='RecibaLaSolicitudDeSelladoElectronicoOdfResponse',
    outputPartName='parameters',
    operationName='RecibaLaSolicitudDeSelladoElectronicoOdf',
    style='document',
)


ValideElServicio_method = xsd.Method(
    soapAction=settings.FVA_HOST + 'ValideElServicio',
    input='ValideElServicio',
    inputPartName='parameters',
    output='ValideElServicioResponse',
    outputPartName='parameters',
    operationName='ValideElServicio',
    style='document',
)


##############################################################################
# SOAP Service


SelladorElectronicoConControlDeLlaveSoap12_SERVICE = soap.Service(
    name='SelladorElectronicoConControlDeLlaveSoap12',
    targetNamespace=settings.FVA_HOST,
    location='${scheme}://${host}/'+settings.SERVICE_URLS['sello'],
    schemas=[Schema_c49e7],
    version=soap.SOAPVersion.SOAP12,
    methods=[RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma_method, RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma_method, RecibaLaSolicitudDeSelladoElectronicoMSOffice_method, RecibaLaSolicitudDeSelladoElectronicoPdf_method, RecibaLaSolicitudDeSelladoElectronicoOdf_method, ValideElServicio_method],
)


##############################################################################
# SOAP Service Stub


class SelladorElectronicoConControlDeLlaveSoap12ServiceStub(soap.Stub, SSLContex):
    SERVICE = SelladorElectronicoConControlDeLlaveSoap12_SERVICE
    SCHEME = settings.STUB_SCHEME
    HOST = settings.STUB_HOST

    def RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma(self, RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma, header=None):
        return self.call('RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma', RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedCoFirma, header=header)

    def RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma(self, RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma, header=None):
        return self.call('RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma', RecibaLaSolicitudDeSelladoElectronicoXmlEnvelopedContraFirma, header=header)

    def RecibaLaSolicitudDeSelladoElectronicoMSOffice(self, RecibaLaSolicitudDeSelladoElectronicoMSOffice, header=None):
        return self.call('RecibaLaSolicitudDeSelladoElectronicoMSOffice', RecibaLaSolicitudDeSelladoElectronicoMSOffice, header=header)

    def RecibaLaSolicitudDeSelladoElectronicoPdf(self, RecibaLaSolicitudDeSelladoElectronicoPdf, header=None):
        return self.call('RecibaLaSolicitudDeSelladoElectronicoPdf', RecibaLaSolicitudDeSelladoElectronicoPdf, header=header)

    def RecibaLaSolicitudDeSelladoElectronicoOdf(self, RecibaLaSolicitudDeSelladoElectronicoOdf, header=None):
        return self.call('RecibaLaSolicitudDeSelladoElectronicoOdf', RecibaLaSolicitudDeSelladoElectronicoOdf, header=header)

    def ValideElServicio(self, ValideElServicio, header=None):
        return self.call('ValideElServicio', ValideElServicio, header=header)

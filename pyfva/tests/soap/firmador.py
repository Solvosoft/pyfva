import unittest
from datetime import timedelta, datetime

from pyfva.clientes.firmador import ClienteFirmador
from ..utils import read_files,  CheckReception

class TestFirmador(unittest.TestCase, CheckReception):
    def setUp(self):
        self.client = ClienteFirmador()

    def firme_documento_default(self, identidad, extension='odf', client=None, resumen='nd', lugar=None, razon=None):
        client = client or self.client

        _format = extension
        if _format == 'bom':
            _format = 'xml_cofirma'
        if lugar or razon:
            doc, hash_doc = read_files('pdf')
            return client.firme(identidad, doc, 'pdf',
                                algoritmo_hash='Sha512',
                                resumen=resumen, id_funcionalidad=-1, lugar=lugar,
                                razon=razon, hash_doc=hash_doc)
        doc, hash_doc = read_files(extension)
        return client.firme(identidad, doc, _format,
                            algoritmo_hash='Sha512', resumen='nd', id_funcionalidad=-1, lugar=lugar,
                            razon=razon, hash_doc=hash_doc)

    def test_valide_servicio(self):
        result = self.client.validar_servicio()
        self.assertTrue(result)

    def test_sign_vacio(self):
        result = self.firme_documento_default("")
        self.assertEqual(result['codigo_error'], 2)

    def test_sign_request_time(self):
        class FakeTimeManager:
            def now(self):
                return datetime.now() + timedelta(days=1)
        client = ClienteFirmador(time_manager=FakeTimeManager())

        result = self.firme_documento_default("01-0123-0456", client=client)
        self.assertEqual(result['codigo_error'], 3)

    def test_sign_not_entity(self):
        client = ClienteFirmador(599,1)
        result = self.firme_documento_default("01-0123-0456", client=client)
        self.assertEqual(result['codigo_error'], 6)

    def test_sign_resume_size_250(self):
        result = self.firme_documento_default("01-0123-0456", resumen="*"*256, lugar="test", razon="test" )
        self.assertEqual(result['codigo_error'], 7)

    def test_sign_razon_size_125(self):
        result = self.firme_documento_default("01-0123-0456", lugar="test", razon="*"*130 )
        self.assertEqual(result['codigo_error'], 8)

    def test_sign_500000000000(self):
        result = self.firme_documento_default("500000000000")
        self.assertEqual(result['codigo_error'], 1)

    def test_sign_0119192222(self):
        result = self.firme_documento_default("01-1919-2222")
        self.assertEqual(result['codigo_error'], 4)

    def test_sign_0119192020(self):
        result = self.firme_documento_default("01-1919-2020")
        self.assertEqual(result['codigo_error'], 5)

    def test_sign_900000000000(self):
        result = self.firme_documento_default("9-0000-0000-000")
        self.assertEqual(result['codigo_error'], 10)

    def test_sign_0119192323(self):
        result = self.firme_documento_default("01-1919-2323")
        self.assertEqual(result['codigo_error'], 11)

    def test_sign_0119192424(self):
        result = self.firme_documento_default("01-1919-2424")
        self.assertEqual(result['codigo_error'], 12)

    def test_sign_0119192525(self):
        result = self.firme_documento_default("01-1919-2525")
        self.assertEqual(result['codigo_error'], 13)

    def test_sign_0119192626(self):
        result = self.firme_documento_default("01-1919-2626")
        self.assertEqual(result['codigo_error'], 14)



   #########################################################
    #  A partir de aca son peticiones con respuestas
    #########################################################

    def test_auth_100000000000(self):
        result = self.firme_documento_default("100000000000")
        self.assertEqual(result['codigo_error'], 0)
        data = self.check_reception(result['id_solicitud'])
        self.assertEqual(data['codigo_error'], 1)

    def test_auth_0110102020(self):
        result = self.firme_documento_default("01-1010-2020")
        self.assertEqual(result['codigo_error'], 0)
        data = self.check_reception(result['id_solicitud'])
        self.assertEqual(data['codigo_error'], 2)

    def test_auth_0120203030(self):
        result = self.firme_documento_default("01-2020-3030")
        self.assertEqual(result['codigo_error'], 0)
        data = self.check_reception(result['id_solicitud'])
        self.assertEqual(data['codigo_error'], 3)

    def test_auth_0140405050(self):
        result = self.firme_documento_default("01-4040-5050")
        self.assertEqual(result['codigo_error'], 0)
        data = self.check_reception(result['id_solicitud'])
        self.assertEqual(data['codigo_error'], 4)



    def test_auth_0160607070(self):
        result = self.firme_documento_default("01-6060-7070")
        self.assertEqual(result['codigo_error'], 0)
        data = self.check_reception(result['id_solicitud'])
        self.assertEqual(data['codigo_error'], 9)

    def test_auth_0180809090(self):
        result = self.firme_documento_default("01-8080-9090")
        self.assertEqual(result['codigo_error'], 0)
        data = self.check_reception(result['id_solicitud'])
        self.assertEqual(data['codigo_error'], 10)

    def test_auth_0111002211(self):
        result = self.firme_documento_default("01-1100-2211")
        self.assertEqual(result['codigo_error'], 0)
        data = self.check_reception(result['id_solicitud'])
        self.assertEqual(data['codigo_error'], 11)

    def test_auth_0133445566(self):
        result = self.firme_documento_default("01-3344-5566")
        self.assertEqual(result['codigo_error'], 0)
        data = self.check_reception(result['id_solicitud'])
        self.assertEqual(data['codigo_error'], 13)

    def test_auth_0177889900(self):
        result = self.firme_documento_default("01-7788-9900")
        self.assertEqual(result['codigo_error'], 0)
        data = self.check_reception(result['id_solicitud'])
        self.assertEqual(data['codigo_error'], 14)

    def test_sign_validate_boom(self):
        result = self.firme_documento_default("01-0123-0456", extension='bom')
        self.assertEqual(result['codigo_error'], 0)
        data = self.check_reception(result['id_solicitud'])
        self.assertEqual(data['codigo_error'], 5)

    def test_documento_invalido(self):
        extension='odf'
        doc, hash_doc = read_files(extension)
        result = self.client.firme("01-0123-0456", doc, 'msoffice',
                            algoritmo_hash='Sha512', resumen='nd', id_funcionalidad=-1,
                              hash_doc=hash_doc)
        self.assertEqual(result['codigo_error'], 0)
        data = self.check_reception(result['id_solicitud'])
        self.assertEqual(data['codigo_error'], 6)

    def test_hash_invalido(self):
        extension='odf'
        doc, hash_doc = read_files(extension, b64=False)
        result = self.client.firme("01-0123-0456", doc, extension,
                            algoritmo_hash='Sha512', resumen='nd', id_funcionalidad=-1,
                              hash_doc=hash_doc)
        self.assertEqual(result['codigo_error'], 0)
        data = self.check_reception(result['id_solicitud'])
        self.assertEqual(data['codigo_error'], 8)


    def test_contrafirma_incorrecta(self):
        doc, hash_doc = read_files('nocontrafirma')
        result = self.client.firme("01-0123-0456", doc, 'xml_contrafirma',
                            algoritmo_hash='Sha512', resumen='nd', id_funcionalidad=-1,
                              hash_doc=hash_doc)
        self.assertEqual(result['codigo_error'], 0)
        data = self.check_reception(result['id_solicitud'])
        self.assertEqual(data['codigo_error'], 15)

    def test_suscriptor_no_conectado(self):
        status = self.client.suscriptor_conectado('05-0387-0668')
        self.assertFalse(status)
        status = self.client.suscriptor_conectado('06-0395-4040')
        self.assertFalse(status)

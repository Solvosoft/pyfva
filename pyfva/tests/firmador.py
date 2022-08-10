import unittest
from datetime import timedelta, datetime

from pyfva.clientes.firmador import ClienteFirmador
from .utils import read_files


class TestFirmador(unittest.TestCase):
    def setUp(self):
        self.client = ClienteFirmador(1,1)

    def firme_documento_default(self, identidad, client=None, resumen='nd', lugar=None, razon=None):
        client = client or self.client

        if lugar or razon:
            return client.firme(identidad, read_files('pdf'), 'pdf',
                                algoritmo_hash='Sha512', hash_doc=None,
                                resumen=resumen, id_funcionalidad=-1, lugar=lugar,
                                razon=razon)

        return client.firme(identidad, read_files('odf'), 'odf',
                            algoritmo_hash='Sha512', hash_doc=None,
                            resumen='nd', id_funcionalidad=-1, lugar=lugar,
                            razon=razon)

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
        client = ClienteFirmador(1,1, time_manager=FakeTimeManager())

        result = self.firme_documento_default("01-0123-0456", client=client)
        self.assertEqual(result['codigo_error'], 3)

    def test_sign_not_entity(self):
        client = ClienteFirmador(1,599)
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

    def test_sign_0119192121(self):
        result = self.firme_documento_default("01-1919-2121")
        self.assertEqual(result['codigo_error'], 9)

    def test_sign_0503870668(self):
        result = self.firme_documento_default("05-0387-0668")
        self.assertEqual(result['codigo_error'], 9)

    def test_sign_0603954040(self):
        result = self.firme_documento_default("06-0395-4040")
        self.assertEqual(result['codigo_error'], 9)

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



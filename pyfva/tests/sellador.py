import unittest

from datetime import timedelta, datetime
from pyfva.clientes.sellador import ClienteSellador
from .utils import read_files


class TestSellador(unittest.TestCase):
    def setUp(self):
        self.client = ClienteSellador()

    def test_1001(self):
        extension='odf'
        doc, hash_doc = read_files(extension)
        result = self.client.firme(doc, extension, algoritmo_hash='Sha512', hash_doc=hash_doc,
              id_funcionalidad=1001)
        self.assertEqual(result['codigo_error'], 1)

    def test_campo_vacio(self):
        extension = 'odf'
        doc, hash_doc = read_files(extension)
        # falta el hash_doc
        result = self.client.firme(doc, extension, algoritmo_hash='Sha512')
        self.assertEqual(result['codigo_error'], 2)

    def test_fecha_invalida(self):

        class FakeTimeManager:
            def now(self):
                return datetime.now() + timedelta(days=1)

        client = ClienteSellador(time_manager=FakeTimeManager())

        extension = 'odf'
        doc, hash_doc = read_files(extension)
        result = client.firme(doc, extension, algoritmo_hash='Sha512', hash_doc=hash_doc,
                                   id_funcionalidad=-1)
        self.assertEqual(result['codigo_error'], 3)

    def test_1004(self):
        extension = 'odf'
        doc, hash_doc = read_files(extension)
        result = self.client.firme(doc, extension, algoritmo_hash='Sha512', hash_doc=hash_doc,
                                   id_funcionalidad=1004)
        self.assertEqual(result['codigo_error'], 4)

    def test_1005(self):
        extension = 'odf'
        doc, hash_doc = read_files(extension)
        result = self.client.firme(doc, extension, algoritmo_hash='Sha512', hash_doc=hash_doc,
                                   id_funcionalidad=1005)
        self.assertEqual(result['codigo_error'], 5)

    def test_sign_not_entity(self):
        client = ClienteSellador(599, 1)
        extension = 'odf'
        doc, hash_doc = read_files(extension)
        result = client.firme(doc, extension, algoritmo_hash='Sha512', hash_doc=hash_doc,
                                   id_funcionalidad=-1)
        self.assertEqual(result['codigo_error'], 6)

    def test_1007(self):
        extension = 'odf'
        doc, hash_doc = read_files(extension)
        result = self.client.firme(doc, extension, algoritmo_hash='Sha512', hash_doc=hash_doc,
                                   id_funcionalidad=1007)
        self.assertEqual(result['codigo_error'], 7)

    def test_1008(self):
        extension = 'odf'
        doc, hash_doc = read_files(extension)
        result = self.client.firme(doc, extension, algoritmo_hash='Sha512', hash_doc=hash_doc,
                                   id_funcionalidad=1008)
        self.assertEqual(result['codigo_error'], 8)

    def test_documento_invalido(self):
        extension='odf'
        doc, hash_doc = read_files(extension)
        result = self.client.firme(doc, 'msoffice', algoritmo_hash='Sha512', id_funcionalidad=-1,
                              hash_doc=hash_doc)
        self.assertEqual(result['codigo_error'], 9)


    def test_hash_invalido(self):
        extension='odf'
        doc, hash_doc = read_files(extension, b64=False)
        result = self.client.firme(doc, extension,
                            algoritmo_hash='Sha512', id_funcionalidad=-1,
                              hash_doc=hash_doc)
        self.assertEqual(result['codigo_error'], 10)

    def test_contrafirma_incorrecta(self):
        doc, hash_doc = read_files('nocontrafirma')
        result = self.client.firme(doc, 'xml_contrafirma',
                            algoritmo_hash='Sha512', id_funcionalidad=-1,
                              hash_doc=hash_doc)
        self.assertEqual(result['codigo_error'], 11)

    def test_sign_razon_size_125(self):
        extension = 'pdf'
        doc, hash_doc = read_files(extension)
        result = self.client.firme(doc, extension, algoritmo_hash='Sha512', hash_doc=hash_doc,
                                   id_funcionalidad=-1, lugar="test", razon="*"*130)
        self.assertEqual(result['codigo_error'], 12)

    def test_1009(self):
        extension = 'odf'
        doc, hash_doc = read_files(extension)
        result = self.client.firme(doc, extension, algoritmo_hash='Sha512', hash_doc=hash_doc,
                                   id_funcionalidad=1009)
        self.assertEqual(result['codigo_error'], 14)

    def test_1010(self):
        extension = 'odf'
        doc, hash_doc = read_files(extension)
        result = self.client.firme(doc, extension, algoritmo_hash='Sha512', hash_doc=hash_doc,
                                   id_funcionalidad=1010)
        self.assertEqual(result['codigo_error'], 15)

    def test_1011(self):
        extension = 'odf'
        doc, hash_doc = read_files(extension)
        result = self.client.firme(doc, extension, algoritmo_hash='Sha512', hash_doc=hash_doc,
                                   id_funcionalidad=1011)
        self.assertEqual(result['codigo_error'], 16)

    def test_documento_sellado(self):

        extension = 'pdf'
        doc, hash_doc = read_files('sellado')
        result = self.client.firme(doc, extension, algoritmo_hash='Sha512', hash_doc=hash_doc,
                                   id_funcionalidad=-1, razon='prueba sellado', lugar='otro lado')
        self.assertEqual(result['codigo_error'], 13)
import unittest
from datetime import timedelta, datetime

from pyfva.clientes.autenticador import ClienteAutenticador
from .utils import CheckReception


class TestAuthenticador(unittest.TestCase, CheckReception):
    def setUp(self):
        self.client = ClienteAutenticador()


    def test_valide_servicio(self):
        result = self.client.validar_servicio()
        self.assertTrue(result)

    def test_auth_vacio(self):
        result = self.client.solicitar_autenticacion("")
        self.assertEqual(result['codigo_error'], 2)

    def test_auth_request_time(self):
        class FakeTimeManager:
            def now(self):
                return datetime.now() + timedelta(days=1)

        client = ClienteAutenticador(time_manager=FakeTimeManager())
        result = client.solicitar_autenticacion("01-0003-0456")
        self.assertEqual(result['codigo_error'], 3)

    def test_auth_not_entity(self):
        client = ClienteAutenticador(negocio=13, entidad=1)
        result = client.solicitar_autenticacion("01-0123-0456")
        self.assertEqual(result['codigo_error'], 6)

    def test_auth_500000000000(self):
        result = self.client.solicitar_autenticacion("500000000000")
        self.assertEqual(result['codigo_error'], 1)

    def test_auth_0119192222(self):
        result = self.client.solicitar_autenticacion("01-1919-2222")
        self.assertEqual(result['codigo_error'], 4)

    def test_auth_0119192020(self):
        result = self.client.solicitar_autenticacion("01-1919-2020")
        self.assertEqual(result['codigo_error'], 5)

    def test_auth_0119192121(self):
        result = self.client.solicitar_autenticacion("01-1919-2121")
        self.assertEqual(result['codigo_error'], 9)

    def test_auth_0503870668(self):
        result = self.client.solicitar_autenticacion("05-0387-0668")
        self.assertEqual(result['codigo_error'], 9)

    def test_auth_0603954040(self):
        result = self.client.solicitar_autenticacion("06-0395-4040")
        self.assertEqual(result['codigo_error'], 9)

    def test_auth_900000000000(self):
        result = self.client.solicitar_autenticacion("9-0000-0000-000")
        self.assertEqual(result['codigo_error'], 10)

    def test_auth_0119192323(self):
        result = self.client.solicitar_autenticacion("01-1919-2323")
        self.assertEqual(result['codigo_error'], 11)

    def test_auth_0119192424(self):
        result = self.client.solicitar_autenticacion("01-1919-2424")
        self.assertEqual(result['codigo_error'], 12)

    def test_auth_0119192525(self):
        result = self.client.solicitar_autenticacion("01-1919-2525")
        self.assertEqual(result['codigo_error'], 13)

    def test_auth_0119192626(self):
        result = self.client.solicitar_autenticacion("01-1919-2626")
        self.assertEqual(result['codigo_error'], 14)

    #########################################################
    #  A partir de aca son peticiones con respuestas
    #########################################################

    def test_auth_nonotificado(self):

        result = self.client.solicitar_autenticacion('01-0129-0129')
        self.assertEqual(result['codigo_error'], 0)
        data = self.check_reception(result['id_solicitud'])
        self.assertEqual(data['codigo_error'], 12)

    def test_auth_100000000000(self):
        result = self.client.solicitar_autenticacion("100000000000")
        self.assertEqual(result['codigo_error'], 0)
        data = self.check_reception(result['id_solicitud'])
        self.assertEqual(data['codigo_error'], 1)

    def test_auth_0110102020(self):
        result = self.client.solicitar_autenticacion("01-1010-2020")
        self.assertEqual(result['codigo_error'], 0)
        data = self.check_reception(result['id_solicitud'])
        self.assertEqual(data['codigo_error'], 2)

    def test_auth_0120203030(self):
        result = self.client.solicitar_autenticacion("01-2020-3030")
        self.assertEqual(result['codigo_error'], 0)
        data = self.check_reception(result['id_solicitud'])
        self.assertEqual(data['codigo_error'], 3)


    def test_auth_0140405050(self):
        result = self.client.solicitar_autenticacion("01-4040-5050")
        self.assertEqual(result['codigo_error'], 0)
        data = self.check_reception(result['id_solicitud'])
        self.assertEqual(data['codigo_error'], 4)

    def test_auth_0160607070(self):
        result = self.client.solicitar_autenticacion("01-6060-7070")
        self.assertEqual(result['codigo_error'], 0)
        data = self.check_reception(result['id_solicitud'])
        self.assertEqual(data['codigo_error'], 9)

    def test_auth_0180809090(self):
        result = self.client.solicitar_autenticacion("01-8080-9090")
        self.assertEqual(result['codigo_error'], 0)
        data = self.check_reception(result['id_solicitud'])
        self.assertEqual(data['codigo_error'], 10)

    def test_auth_0111002211(self):
        result = self.client.solicitar_autenticacion("01-1100-2211")
        self.assertEqual(result['codigo_error'], 0)
        data = self.check_reception(result['id_solicitud'])
        self.assertEqual(data['codigo_error'], 11)

    def test_auth_0133445566(self):
        result = self.client.solicitar_autenticacion("01-3344-5566")
        self.assertEqual(result['codigo_error'], 0)
        data = self.check_reception(result['id_solicitud'])
        self.assertEqual(data['codigo_error'], 13)

    def test_auth_0177889900(self):
        result = self.client.solicitar_autenticacion("01-7788-9900")
        self.assertEqual(result['codigo_error'], 0)
        data = self.check_reception(result['id_solicitud'])
        self.assertEqual(data['codigo_error'], 14)
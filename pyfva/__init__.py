
from importlib import import_module

from .clientes.autenticador import ClienteAutenticador
from .clientes.firmador import ClienteFirmador
from .clientes.validador import ClienteValidador
from .clientes.verificador import ClienteVerificador


def load_module_responder(module):
    return import_module(module)

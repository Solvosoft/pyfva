
from importlib import import_module

from .clientes.autenticador import ClienteAutenticador
from .clientes.firmador import ClienteFirmador
from .clientes.validador import ClienteValidador
from .clientes.verificador import ClienteVerificador
from .clientes.sellador import ClienteSellador

def load_module_responder(module):
    return import_module(module)

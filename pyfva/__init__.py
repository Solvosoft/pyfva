
from importlib import import_module
from .conf import settings

if settings.DEFAULT_CONNECTION_TYPE == 'soap':
    from .clientes.validador import ClienteValidador
    from .clientes.verificador import ClienteVerificador
    from .clientes.sellador import ClienteSellador

from .clientes.autenticador import ClienteAutenticador
from .clientes.firmador import ClienteFirmador


def load_module_responder(module):
    return import_module(module)

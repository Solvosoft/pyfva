
from pyfva.conf import settings

if settings.DEFAULT_CONNECTION_TYPE == 'soap':
    from .soap.autenticador import ClienteAutenticador
elif settings.DEFAULT_CONNECTION_TYPE == 'rest':
    from .rest.autenticador import ClienteAutenticador

__all__ = ['ClienteAutenticador']
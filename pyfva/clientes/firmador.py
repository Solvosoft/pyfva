
from pyfva.conf import settings

if settings.DEFAULT_CONNECTION_TYPE == 'soap':
    from .soap.firmador import ClienteFirmador
elif settings.DEFAULT_CONNECTION_TYPE == 'rest':
    from .rest.firmador import ClienteFirmador

__all__ = ['ClienteFirmador']
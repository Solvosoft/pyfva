from pyfva.conf import settings
if settings.DEFAULT_CONNECTION_TYPE == 'soap':
    from .soap.autenticador import *
    from .soap.firmador import *
    from .soap.sellador import *
elif settings.DEFAULT_CONNECTION_TYPE == 'rest':
    from .rest.autenticador import *
    from .rest.firmador import *
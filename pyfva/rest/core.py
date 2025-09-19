from pytz import timezone
from pyfva.conf import settings
from datetime import datetime
import os
class BCCRRestClient:
    def __init__(self,
                 negocio=settings.DEFAULT_BUSSINESS,
                 entidad=settings.DEFAULT_ENTITY, time_manager=None):
        self.negocio = negocio
        self.entidad = entidad
        self.time_manager = time_manager or datetime

    def get_requests_extra_headers(self):
        #return {}
        return {
            "cert": (os.getenv('REQUESTS_CERT_PATH'), os.getenv('REQUESTS_KEY_PATH')),
        }

    def get_now(self):
        gtm6 = timezone(settings.PYFVA_TIMEZONE)
        return gtm6.localize(self.time_manager.now()).isoformat() #.strftime('%Y-%m-%dT%H:%M:%S')
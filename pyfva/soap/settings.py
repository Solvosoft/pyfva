'''
Created on 24 jul. 2017

@author: luis
'''


FVA_HOST = "http://bccr.fva.cr/"
# FVA_HOST = 'http://bccr.fva.cr/'
STUB_SCHEME = 'http'
STUB_HOST = "localhost:8001"
#RECEPTOR_HOST = "http://localhost:8000/"
RECEPTOR_HOST = 'http://bccr.fva.cr/'

RECEPTOR_CLIENT = 'pyfva.receptor.client'

DEFAULT_BUSSINESS = 1
DEFAULT_ENTITY = 1

import sys
import os


def load_settings(settings):
    thismodule = sys.modules[__name__]

    for name in ['FVA_HOST',
                 'STUB_SCHEME',
                 'STUB_HOST',
                 'RECEPTOR_HOST',
                 'DEFAULT_BUSSINESS',
                 'DEFAULT_ENTITY',
                 'RECEPTOR_CLIENT']:

        if hasattr(settings, name):
            setattr(thismodule, name,
                    getattr(settings, name)
                    )
        elif name in settings:
            setattr(thismodule, name,
                    settings[name]
                    )


try:
    from django.conf import settings as djsettings
    load_settings(djsettings)
except:
    pass

load_settings(os.environ)

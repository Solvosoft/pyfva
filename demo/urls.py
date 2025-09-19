"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings

from demo.views import json_wrapper
from pyfva.receptor import rest
from pyfva.receptor.ws_service import ResultadoDeSolicitudSoap_SERVICE
from soapfish.django_ import django_dispatcher
dispatcher = django_dispatcher(ResultadoDeSolicitudSoap_SERVICE)
import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('check_transaction/<int:idtransaction>', views.check_transaction ),
    path(settings.DEFAULT_NOTIFICATION_URL, dispatcher),
    path('rest/NotifiqueLaRespuesta', json_wrapper(rest.recibe_notificacion)),
    path('rest/ValideElServicio', json_wrapper(rest.valide_servicio_view)),
]

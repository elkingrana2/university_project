from django.contrib import admin
from django.urls import path
from Modulos.Academica.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacto/', contacto),
    #path('contactar/', contactar)
] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)

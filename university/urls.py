from django.contrib import admin
from django.urls import path
from Modulos.Academica.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacto/', contacto),
    #path('contactar/', contactar)
] 

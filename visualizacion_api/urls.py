"""
URL configuration for visualizacion_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
#from django.contrib import admin
#from django.urls import path

#urlpatterns = [
    #path('admin/', admin.site.urls),
#]

from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from visualizacion_api.views import visualizar_dataset

# Función que redirige la raíz '/'
def redirect_root(request):
    # Redirige a la API de visualización
    return redirect('visualizar_dataset')
    # O, si quieres al front-end:
    # return redirect('https://tu-front-end-url.com')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/visualizar/', visualizar_dataset, name='visualizar_dataset'),
    path('', redirect_root),  # <- usar la función definida arriba
]




"""
URL configuration for ultima project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from base.views import *

urlpatterns = [
    path('', inicio, name='inicio'),

    path('contato/', contato, name='contato'),
    path('reserva/', reserva , name='reserva'),
    path('api/', apis_disp, name='api'),
    #include('reserva.urls', namespace='reserva')

    # Login e cadastro de Usuário
    path('login/', login_usuario, name='login_usuario'),
    path('logout/', logout_usuario, name='logout_usuario'),
    path('novo-usuario/', novo_usuario, name='novo_usuario'),

    path('admin/', admin.site.urls, name='adm'),
    path('apt-auth/', include('rest_framework.urls')),
    path('api/', include('rest_api.urls', namespace='api')),
]

from django.urls import path, include

from rest_api.views import contatos, reservas


app_name = 'rest_api'

urlpatterns = [
    path('contatos/', contatos, name='contatos'),
    path('reservas/', reservas, name='reservas')
]
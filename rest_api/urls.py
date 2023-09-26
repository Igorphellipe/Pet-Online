from django.urls import path, include

from rest_api.views import contatos, reservas, AgendamentoModelViewSet, ContatoModelViewSet

from rest_framework.routers import SimpleRouter


app_name = 'rest_api'

router = SimpleRouter(trailing_slash=False)
router.register('reservas', AgendamentoModelViewSet)
router.register('contatos', ContatoModelViewSet)


urlpatterns = [
    path('contatos/', contatos, name='contatos'),
    path('reservas/', reservas, name='reservas')
]

urlpatterns += router.urls
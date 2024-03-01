from django.urls import path, include

from rest_api.views import PetshopModelViewSet, AgendamentoModelViewSet, ContatoModelViewSet, PorteAnimalModelViewSet

from rest_framework.routers import SimpleRouter


app_name = 'rest_api'

router = SimpleRouter(trailing_slash=False)
router.register('agenda', AgendamentoModelViewSet)
router.register('contato', ContatoModelViewSet)
router.register('petshop', PetshopModelViewSet)
router.register('agenda-porte', PorteAnimalModelViewSet)

urlpatterns = router.urls

'''urlpatterns = [
    path('contatos/', contatos, name='contatos'),
    path('reservas/', reservas, name='reservas'),
]

urlpatterns += router.urls
'''
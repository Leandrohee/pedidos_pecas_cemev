# aqui sera administrado as urls responsaveis pela parte dos pedidos das oficinas

from django.urls import path, include
from .views import renderizandoReact
from .serializer_views import Pedido2024ViewSet
from rest_framework import routers

router = routers.DefaultRouter()                                                                #criando uma rota base para acessar a api 
router.register(r'pedidos2024', Pedido2024ViewSet, basename='pedidos2024')                      #criando a rota relativa 'pedidos2024/' para acessar o modelo Pedido2024 com o serializer


urlpatterns = [
    path('',include(router.urls)),                                                              #essa rota padrao direciona para as rotas relativas criadas usando o viewset
    path('',renderizandoReact, name='pedidosOficina'),
]
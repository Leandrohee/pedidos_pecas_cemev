# aqui sera administrado as urls responsaveis pela parte dos pedidos das oficinas

from django.urls import path
from .views import renderizandoReact

urlpatterns = [
    path('',renderizandoReact, name='pedidosOficina'),
]
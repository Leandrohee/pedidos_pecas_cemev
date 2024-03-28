#aqui eh onde vamos fazer as funcoes que vao enviar dados para as paginas html
#a visualizações dos serializaçoes fica no arquivo serializer_views.py

from django.shortcuts import render
from rest_framework import viewsets                                                                 #importando  o viewset que fara a disponibilizacao dos objetos do banco de dados no formato JSON
from .models import Pedido2024
from .serializer import Pedido2024Serializer

def renderizandoReact(request):                                                             #essa funcao eh responsavel por renderizar o index.html base no react
    return render(request, 'index.html')


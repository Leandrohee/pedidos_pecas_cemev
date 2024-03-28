#ao inves de colocar as visualizaçoes dos serializers no arquivo views.py criei esse arquivo somente dedicado para visualizaçoes de serializers

from rest_framework import viewsets                                                                 #importando  o viewset que fara a disponibilizacao dos objetos do banco de dados no formato JSON
from rest_framework import views, response, generics                                                #o views e reponse são necessarios no APIView o generics é necessario no listAPiView      
from rest_framework import authentication, permissions                                              #importando as permissoes e autenticacoes neceesarioas para visualizar os serializers
from .models import Pedido2024                                                                      #importando o modelo Pedido do banco de dados
from .serializer import Pedido2024Serializer                                                        #importando o serializers

class ClasseDeAutenticacao(viewsets.ModelViewSet):                                                  #ESSA CLASSE EU QUE CRIEI COM INTUITO DE EVITAR CODIGO GRANDE E REPETIDO E ELA SERVIRA PARA HERDAR O "viewsets.ModelViewSet" E ACRESCENTAR A SEGURANCA QUE FICA EM TDS AS OUTRAS CLASSES
    authentication_classes =  [authentication.BasicAuthentication]                                  #autenticacao basica para a API
    permission_classes = [permissions.IsAuthenticated]                                              #somente acessa essa classe quem esta autenticado|logado


class Pedido2024ViewSet(ClasseDeAutenticacao):                                                     #essa eh a classe responsavel por disponizilizar a visualizacao do modelo Pedido2024
    queryset = Pedido2024.objects.all()
    serializer_class = Pedido2024Serializer





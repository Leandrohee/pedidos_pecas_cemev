#Nesse arquivo sao criados os serializers que sao os tratudores entre django e Json 
#Esses 'dicionarios' sao importantes pois  geralmente as API's sao em JSON e o backend e escrito  em python

from rest_framework import serializers                                          #importando  o serializer do rest_framework
from  .models import Pedido2024                                                 #importando os modelos do DB criandos em python


class Pedido2024Serializer(serializers.ModelSerializer):                        #Essa classe vai serializar os modelos do DB, ou seja transformar eles em JSON
    
    ''''TRADUZINDO OS CAMPOS PARA MOSTRAR A OPCAO MAIS LEGIVEL AO INVES DE SIMPLESMENTE O ID'''
    
    oficina = serializers.SerializerMethodField()                                   #pega o nome adequado pra visualizar na api. Necesasrio passar pela funcao get_oficina tb
    modelo = serializers.SerializerMethodField()                                    #pega o nome adequado pra visualizar na api. Necesasrio passar pela funcao get_modelo tb
    prefixo = serializers.SerializerMethodField()                                   #pega o nome adequado pra visualizar na api. Necesasrio passar pela funcao get_prefixo tb

    def get_oficina(self,obj):                                                      #essa funcao eh responsavel por puxar qual oficina foi selecionado no objeto especifico. Tem que ter o mesmo nome do campo referente no models  precedido de get_
        return obj.get_oficina_display()                                            #esse retorno vai para variavel lá em cima oficina

    def get_modelo(self,obj):                                                       #essa funcao eh responsavel por puxar qual modelo foi selecionado no objeto especifico. Tem que ter o mesmo nome do campo referente no models  precedido de get_
        return obj.get_modelo_display()                                             #esse retorno vai para variavel lá em cima modelo
    
    def get_prefixo(self,obj):                                                      #essa funcao eh responsavel por puxar qual modelo foi selecionado no objeto especifico. Tem que ter o mesmo nome do campo referente no models  precedido de get_
        return obj.get_prefixo_display()                                            #esse retorno vai para variavel lá em cima modelo
    
    '''FINAL DA TRADUCAO DOS CAMPOS'''

    class Meta:
        model = Pedido2024                                                      #aqui escolhemos qual eh o modelo que queremos serializar
        fields = ['id',                                                         #aqui escolhemos quais propriedades queremos disponibilizar
                  'pedido',  
                  'oficina',
                  'oss',
                  'modelo',
                  'prefixo',
                ]                                                     
        # fields = '__all__'                                                        #se nao quisersmos colocar todas as propriedades colocamos dessa forma somente as que queremos diponibilizar

  


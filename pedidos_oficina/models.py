# Nesse arquivo é onde se configura os modelos para o banco de dados
# O caminho da criacao do model ate a sua disponibilizacao em uma URL eh a seguinte: models --> serializer --> serializer_views --> urls
# O caminho da criacao do model ate a sua disponibilizacao no campo ADMIN eh a seguiinte: models --> admin

from django.db import models
from django.db import connections                                                                                       #para fazer a conexao com o banco de dados
from django.core.validators import RegexValidator

def pegandoPrefixosDoDb():                                                                                              #criei uma funcao que fara a captura dos dados no meu bancod e dados
    conexao_db = connections['default']                                                                                 #faz uma coneccao com o banco de dados

    with conexao_db.cursor() as cursor:                                                     
        cursor.execute(f"SELECT prefixo FROM viaturas")                                                                 #esse codigo eh em sql pega somente os dados da coluna "prefixo" da tabela 'viaturas'
        prefixos = cursor.fetchall()                                                                                    #comando para pegar todos os dados da coluna 
        prefixos = tuple(prefixos)                                                                                      #transforma os dados obtidos em uma tupla --> ()                

        prefixos_com_id = tuple((str(i+1),item[0]) for i, item in enumerate(prefixos))                                  #pega a tupla extraida do banco de dados e coloca um id em cada uma, pq esse eh o formato que o parametro choices suporta
        
        return prefixos_com_id                                                                                          #retorna a tupla para a funcao


def pegandoModelosDoDb():                                                                                               #criei uma funcao que fara a captura dos modelos de viaturas no meu banco de dados
    conexao_db = connections['default']                                                                                 #faz uma coneccao com o banco de dados

    with conexao_db.cursor() as cursor:                                                     
        cursor.execute(f"SELECT modelo FROM viaturas")                                                                  #esse codigo eh em sql pega somente os dados da coluna "modelo" da tabela 'viaturas'
        modelos = cursor.fetchall()                                                                                     #comando para pegar todos os dados da coluna
        modelos_sem_repetir = tuple(set(modelos))                                                                       #retira todos os itens repetidos em uma tupla e cria uma nova tupla
        modelos_ordenados = tuple(sorted(modelos_sem_repetir))                                                          #ordena os itens da tupla em ordem numerica e alfabetica e cria uma nova tupla
        modelos_com_id = tuple( (str(i+1),item[0]) for i, item in enumerate(modelos_ordenados) )                        #coloca um id em cada uma das tuplas internas
        
        return modelos_com_id                                                                                           #retorna a tupla para a funcao


class Pedido2024(models.Model):

    OFICINAS = (                                                                                                        #O primeiro parametro eh o que vai ficar guardado no banco de dados o segundo parametro eh para um humano ler
        ('gasolina', 'GASOLINA'),
        ('diesel', 'DIESEL'),
        ('posto','POSTO'),
        ('eletrica','ELÉTRICA'),
        ('montagem', 'MONTAGEM'),
        ('motos', 'MOTOS'),
        ('superestruturas', 'SUPERESTRUTURAS'),
        ('borracharia', 'BORRACHARIA'),
        ('pintura', 'PINTURA'),
    )

    OS_VALIDATOR = RegexValidator(                                                                                      #valindado a os para ter o seguinte formato: 1234/2024
        regex= r'\d{1,4}\s?\/\s?\d{2,4}',                                                                               #regex referente a validação
        message= 'Formato invalido. Correto: 1234/2024',
        code= 'invalid_os_format'
    )

    NOME_FORNECEDOR = (                                                                                                 #O primeiro parametro eh o que vai ficar guardado no banco de dados o segundo parametro eh para um humano ler
        ('gilson', 'GILSON'),
        ('partslub','PARTS LUB'),
    )

    PREFIXOS  = pegandoPrefixosDoDb()

    MODELOS = pegandoModelosDoDb()


    pedido = models.IntegerField(default=1, editable=False)                                                                                                 #significa que o default desse pedido eh 1 e que ele nao pode ser editavel
    oficina = models.CharField(max_length=30 ,choices=OFICINAS, blank=False, null=False, default='')                                                        #multiplas funcoes de oficinas setadas na variavel  OFICINAS
    oss = models.CharField(max_length=11, blank=False, null=False,validators=[OS_VALIDATOR])                                                                                           #quero add depois a funcao de somente ler O.S nesse  formato: 0000/2024     
    prefixo = models.CharField(max_length=10, choices=PREFIXOS, blank=False, null=False, default='')                                                        #quero que somente apareca os prefixos do banco de dados
    modelo =  models.CharField(max_length=30, choices=MODELOS , blank=False, null=False, default='')
    fornecedor = models.CharField(max_length=30, choices=NOME_FORNECEDOR, blank=False, null=False, default='')
    data_envio = models.DateField()                                                                                               #formato da data: '15/11/1994'
    data_recebimento = models.DateField(blank=True)                                                                             #formato da data: '15/11/1994'
    responsavel_recebimento = models.CharField(max_length=9, blank=True)
    mecanico_requerente = models.CharField(max_length=9, blank=True)
    nota_fiscal = models.CharField(max_length=9, blank=True)

    def save(self, *args, **kwargs):                                                            # Sobrescreve o método save para garantir que o campo numero seja atualizado corretamente
        if not self.pk:                                                                         # Verifica se o objeto é novo e se está sendo criado pela primeira vez (ainda não tem chave primária)
            ultimo_pedido = Pedido2024.objects.order_by('-pedido').first()                      # Coloca os pedidos em ordem decrescente e obtém o primeiro item desta lista decrescente. Em resumo pega o maior numero
            if ultimo_pedido == None:                                                           # Se for igual a None quer dizer que nenhum pedido ainda foi feito
                self.pedido = 1                                                                 # Se nenhum pedido ainda foi feito colocar esse primeiro pedido com o numero 1
            else:
                self.pedido = ultimo_pedido.pedido + 1                                          # Incrementa o número baseado no último objeto     
        super().save(*args, **kwargs)                                                           # Chama o método save padrão para salvar o objeto

    def __str__(self):
        return (f'Pedido {self.pedido}')

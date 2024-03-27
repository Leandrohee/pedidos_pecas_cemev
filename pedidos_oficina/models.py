from django.db import models
from django.db import connections                                                                                       #para fazer a conexao com o banco de dados

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

    NOME_FORNECEDOR = (                                                                                                 #O primeiro parametro eh o que vai ficar guardado no banco de dados o segundo parametro eh para um humano ler
        ('gilson', 'GILSON'),
        ('partslub','PARTS LUB'),
    )

    PREFIXOS  = pegandoPrefixosDoDb()

    MODELOS = pegandoModelosDoDb()


    oficina = models.CharField(max_length=30 ,choices=OFICINAS, blank=False, null=False, default='')                                                        #multiplas funcoes de oficinas setadas na variavel  OFICINAS
    oss = models.CharField(max_length=9, blank=False, null=False)                                                                                           #quero add depois a funcao de somente ler O.S nesse  formato: 0000/2024     
    prefixo = models.CharField(max_length=10, choices=PREFIXOS, blank=False, null=False, default='')                                                                                       #quero que somente apareca os prefixos do banco de dados
    modelo =  models.CharField(max_length=30, choices=MODELOS , blank=False, null=False, default='')
    fornecedor = models.CharField(max_length=30, choices=NOME_FORNECEDOR, blank=False, null=False, default='')
    data_envio = models.DateField()
    data_recebimento = models.DateField()
    responsavel_recebimento = models.CharField(max_length=9, blank=False, null=False)
    mecanico_requerente = models.CharField(max_length=9, blank=False, null=False)
    nota_fiscal = models.CharField(max_length=9, blank=False, null=False)

    def __str__(self):
        return (f'Pedido {self.id}')

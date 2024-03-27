from django.db import models
from django.db import connections

def pegandoPrefixosDoDb():
    table_viaturas = 'viaturas'
    coluna_viaturas = 'prefixo'
    conexao_db = connections['default']

    with conexao_db.cursor() as cursor:
        cursor.execute(f"SELECT {coluna_viaturas} FROM {table_viaturas}")
        prefixos = cursor.fetchall()
        prefixos = tuple(prefixos)

        return prefixos

class Pedido2024(models.Model):

    OFICINAS = (
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

    NOME_FORNECEDOR = (
        ('gilson', 'GILSON'),
        ('partslub','PARTS LUB'),
    )

    PREFIXOS  = pegandoPrefixosDoDb()

    print(OFICINAS)


    oficina = models.CharField(max_length=30 ,choices=OFICINAS, blank=False, null=False, default='')                                                        #multiplas funcoes de oficinas setadas na variavel  OFICINAS
    oss = models.CharField(max_length=9, blank=False, null=False)                                                                                           #quero add depois a funcao de somente ler O.S nesse  formato: 0000/2024     
    prefixo = models.CharField(max_length=10,choices=PREFIXOS, blank=False, null=False, default='')                                                                                       #quero que somente apareca os prefixos do banco de dados
    modelo =  models.CharField(max_length=20, blank=False, null=False)
    fornecedor = models.CharField(max_length=30, choices=NOME_FORNECEDOR, blank=False, null=False, default='')
    data_envio = models.DateField()
    data_recebimento = models.DateField()
    responsavel_recebimento = models.CharField(max_length=9, blank=False, null=False)
    mecanico_requerente = models.CharField(max_length=9, blank=False, null=False)
    nota_fiscal = models.CharField(max_length=9, blank=False, null=False)

    def __str__(self):
        return (f'Pedido {self.id}')

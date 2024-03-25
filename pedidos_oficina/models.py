from django.db import models

class Pedido(models.Model):

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

    oficina = models.CharField(max_length=30 ,choices=OFICINAS, blank=False, null=False, default='')
    oss = models.CharField(max_length=9, blank=False, null=False)  
    prefixo = models.CharField(max_length=9, blank=False, null=False)  
    modelo =  models.CharField(max_length=20, blank=False, null=False)
    fornecedor = models.CharField(max_length=30, choices=NOME_FORNECEDOR, blank=False, null=False, default='')
    data_envio = models.DateField()
    data_recebimento = models.DateField()
    responsavel_recebimento = models.CharField(max_length=9, blank=False, null=False)
    mecanico_requerente = models.CharField(max_length=9, blank=False, null=False)
    nota_fiscal = models.CharField(max_length=9, blank=False, null=False)

    def __str__(self):
        return (f'Pedido {self.id}')

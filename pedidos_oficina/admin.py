from django.contrib import admin
from .models import Pedido2024

class PedidoAdmin2024(admin.ModelAdmin):
    
    list_display = ('id','oficina','oss','prefixo','modelo','fornecedor', 'data_envio','data_recebimento','responsavel_recebimento','mecanico_requerente','nota_fiscal')
    list_display_links = ('id',)
    search_fields = ('id','prefixo')
    list_per_page = 100


admin.site.register(Pedido2024,PedidoAdmin2024)


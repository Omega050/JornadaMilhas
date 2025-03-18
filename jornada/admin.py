from django.contrib import admin
from .models import Depoimento, Destino

@admin.register(Depoimento)
class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'depoimento', 'imagem')

@admin.register(Destino)
class DestinoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'imagem', 'imagem2', 'meta', 'texto_descritivo', 'preco', 'preco_currency')

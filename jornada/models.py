from djmoney.models.fields import MoneyField
from django.db import models
from djmoney.models.validators import  MinMoneyValidator

class Depoimento(models.Model):
    nome = models.CharField(max_length=30, blank=False, null=False)
    depoimento = models.CharField(max_length=100, blank=False, null=False)
    imagem = models.ImageField(upload_to='depoimentos/', blank=False, null=False)
    
    def __str__(self):
        return self.nome

class Destino(models.Model):
    nome = models.CharField(max_length=30, blank=False, null=False)
    imagem = models.ImageField(upload_to='destinos/', blank=False, null=False)
    imagem2 = models.ImageField(upload_to='destinos/', blank=False, null=False)
    preco = MoneyField(
        decimal_places=2,
        default=0,
        default_currency='BRL',  
        max_digits=11,
        validators =
        [
            MinMoneyValidator(0, message='Valor inválido. O valor não pode ser negativo',)
        ],
    )
    meta = models.CharField(max_length=160, null=False, blank=False)
    texto_descritivo = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
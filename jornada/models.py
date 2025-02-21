from django.db import models

class Depoimento(models.Model):
    nome = models.CharField(max_length=30)
    depoimento = models.TextField
    imagem = models.ImageField
    
    def __str__(self):
        return self.nome

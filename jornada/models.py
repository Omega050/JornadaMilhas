from django.db import models

class Depoimento(models.Model):
    nome = models.CharField(max_length=30, blank=False, null=False)
    depoimento = models.CharField(max_length=100, blank=False, null=False)
    imagem = models.ImageField(upload_to='depoimentos/', blank=False, null=False)
    
    def __str__(self):
        return self.nome

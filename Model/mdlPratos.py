from django.db import models

class Prato(models.Model):
    nome = models.CharField(max_length=255)
    modo_preparo = models.TextField()
    ingredientes = models.TextField()
    calorias = models.IntegerField()
    imagem = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return self.nome
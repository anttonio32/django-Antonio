from django.db import models

# Create your models here.
class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    tel = models.CharField(max_length=11)

    def __str__(self):
        return self.nome

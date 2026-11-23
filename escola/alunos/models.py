from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=10)
    idade = models.IntegerField()
    email = models.EmailField()
    endereco = models.CharField(max_length=200)
    tel = models.CharField(max_length=11)

    def __str__(self):
        return self.nome

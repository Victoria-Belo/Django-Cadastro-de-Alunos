from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Base(models.Model):
    at_create = models.DateTimeField(auto_now_add=True)
    at_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Aluno(Base):
    matricula = models.IntegerField()
    cpf = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999999999)])
    nome = models.CharField(max_length=80)
    email = models.EmailField(max_length=80, blank=True)
    telefone = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999999999)])

    class Meta:
        ordering = ['cpf', 'nome', 'matricula', 'email', 'telefone']

    def __str__(self):
        return self.nome

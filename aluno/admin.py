from django.contrib import admin
from aluno.models import Aluno


@admin.register(Aluno)
class alunoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'cpf', 'email', 'telefone')

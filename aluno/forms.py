from django.forms import ModelForm
from aluno.models import Aluno
from django import forms


class alunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'

    matricula = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'matricula'}))
    cpf = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control' , 'id': 'cpf'}))
    nome = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'nome'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}))
    telefone = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'telefone'}))

from django.shortcuts import render, get_object_or_404
from aluno.forms import *
from django.contrib import messages
from django.shortcuts import redirect
from aluno.models import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

/*
*Victória Belo
*
*/

def index(request):
    form = alunoForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print('->', form)
            messages.success(request, 'Registro realizado com sucesso')
            form.save()
            redirect('/')
        else:
            print("erro!", form)
            messages.error(request, 'Erro!')

    alunos = Aluno.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(alunos, 4)
    try:
        alunos = paginator.page(page)
    except PageNotAnInteger:
        alunos = paginator.page(1)
    except EmptyPage:
        alunos = paginator.page(paginator.num_pages)

    context = {
        'lista_aluno': alunos,
        'form': form,
        'users': alunos
    }

    return render(request, 'index.html', context)


def editar(request):
    # 1) informa dados que pretende editar (matricula como id);
    # 2) pegar matricula e encontra-la na lista;
    # 3) SE encontrado na lista, altera-la;

    # aluno = Aluno.objects.get(matricula=request.matricula)
    post = get_object_or_404(alunoForm)
    if str(request.method) == "POST":
        aluno = alunoForm(request.POST or None)
        if aluno.is_valid():
            post = aluno.save()
    else:
        aluno = alunoForm(instance=post)

    context = {
        'edicao_aluno': post

    }
    return render(request, context)

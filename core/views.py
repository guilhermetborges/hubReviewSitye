from django.shortcuts import render, get_object_or_404 ,redirect
from django.contrib import messages

from .forms import FormsForm, ProdutoModelForm
from .models import Produto


def index(request):
    context = {
        'produtos': Produto.objects.all()
    }

    return render(request, 'index.html',context)


def contato(request):
    form = FormsForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem enviada com sucesso!')
            form = FormsForm()
        else:
            messages.error(request, 'Erro ao enviar mensagem!')
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request, 'Produto cadastrado com sucesso!')
            form = ProdutoModelForm()

        else:
            messages.error(request, 'Erro ao cadastrar produto!')
    else:
        form = ProdutoModelForm()

    context = {
        'form': form
    }

    return render(request, 'produto.html', context)


def avaliacoes(request):
    query = request.GET.get('q') ## Pega o valor do campo de busca
    if query:
        produtos = Produto.objects.filter(nome__icontains=query) ## Filtra os produtos pelo nome
    else:
        ## Se não houver valor no campo de busca, retorna todos os produtos
        ## Caso contrário, retorna os produtos filtrados pelo nome
        produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'avaliacoes.html', context)
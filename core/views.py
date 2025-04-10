from django.shortcuts import render, get_object_or_404 ,redirect
from django.contrib import messages

from .forms import FormsForm, ProdutoModelForm
from .models import Produto, Forms
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class IndexView(TemplateView):
    template_name = 'index.html'


class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoModelForm
    template_name = 'produto.html'
    success_url = reverse_lazy('produto-create')

    def form_valid(self, form):
        messages.success(self.request, 'Produto cadastrado com sucesso!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao cadastrar produto!')
        return super().form_invalid(form)


class ContatoView(CreateView):
    model = Forms
    form_class = FormsForm
    template_name = 'contato.html'
    success_url = reverse_lazy('contato')

    def form_valid(self, form):
        messages.success(self.request, 'Mensagem enviada com sucesso!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao enviar mensagem!')
        return super().form_invalid(form)
    


class ContatoView(CreateView):
    model = Forms
    form_class = FormsForm
    template_name = 'contato.html'
    success_url = reverse_lazy('contato')

    def form_valid(self, form):
        messages.success(self.request, 'Mensagem enviada com sucesso!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao enviar mensagem!')
        return super().form_invalid(form)
    

class ProdutoListView(ListView):
    model = Produto
    template_name = 'avaliacoes.html'
    context_object_name = 'produtos'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Produto.objects.filter(nome__icontains=query)
        return Produto.objects.all()




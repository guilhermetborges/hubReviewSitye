from django.shortcuts import render, get_object_or_404 ,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from .forms import FormsForm, ProdutoModelForm, UsuarioRegisterForm
from .models import Produto, Forms , Usuario
from django.views.generic import TemplateView , View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        messages.error(request, 'Usuário ou senha inválidos')
        return render(request, self.template_name)

class UserRegisterView(CreateView):
    model = Usuario
    form_class = UsuarioRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'logout.html')
    
    def post(self, request):
        logout(request)
        return render(request, 'logout.html')

class IndexView(TemplateView):
    template_name = 'index.html'


class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoModelForm
    template_name = 'produto.html'
    success_url = reverse_lazy('produto')

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
    



class ProdutoListView(ListView):
    model = Produto
    paginate_by = 8
    ordering = ['id']  
    template_name = 'avaliacoes.html'
    context_object_name = 'produtos'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(nome__icontains=q)
        return queryset



from django.contrib import admin
from .models import Produto, Forms , Usuario
from .forms import UsuarioRegisterForm

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    form = UsuarioRegisterForm
    model = Usuario


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco','slug', 'criado', 'modificado', 'ativo')



@admin.register(Forms)
class FormsAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email','assunto', 'mensagem', 'criado' )



from django.contrib import admin
from .models import Produto, Forms
 

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco','slug', 'criado', 'modificado', 'ativo')



@admin.register(Forms)
class FormsAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email','assunto', 'mensagem', 'criado' )



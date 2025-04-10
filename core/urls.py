from django.urls import path

from .views import IndexView , ProdutoCreateView, ProdutoListView, ContatoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('produto/', ProdutoCreateView.as_view(), name='produto'),
    path('avaliacoes/', ProdutoListView.as_view(), name='avaliacoes'),
]
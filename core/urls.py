from django.urls import path

from .views import IndexView , ProdutoCreateView, ProdutoListView, ContatoView , LoginView , LogoutView , UserRegisterView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('produto/', ProdutoCreateView.as_view(), name='produto'),
    path('avaliacoes/', ProdutoListView.as_view(), name='avaliacoes'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),

]
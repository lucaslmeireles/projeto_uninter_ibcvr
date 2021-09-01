from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.PagInicial.as_view(), name='index'),
    path('adicionarcontato/', views.adicionacontato, name='adicionar'),
]

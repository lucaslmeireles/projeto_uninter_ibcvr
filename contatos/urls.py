from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.paginicio, name='paginicio'),
    path('sobre/', views.paginicio, name='sobre'),
    path('agenda/', views.PagInicialAgenda.as_view(), name='index'),
    path('adicionarcontato/', views.adicionacontato, name='adicionar'),
    path('enviaremail/', views.enviaemail, name='enviaemail'),
]

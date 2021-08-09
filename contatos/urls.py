from django.urls import path, include
from django.views.generic import TemplateView
from . import views
import contatos



urlpatterns = [
    path('', views.PagInicial.as_view(), name='paginicial'),
]

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class PagInicial(LoginRequiredMixin, ListView):
    model = models.Contato
    template_name = 'contatos/index.html'
    login_url = 'perfil/login/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'contatos'
    paginate_by = 10
    

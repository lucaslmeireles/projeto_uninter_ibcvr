from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Categoria, Contato
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class PagInicial(LoginRequiredMixin, ListView):
    model = Contato
    template_name = 'contatos/index.html'
    login_url = 'perfil/login/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'contatos'
    paginate_by = 10
    
def adicionacontato(request):
    if request.method != 'POST':
        return render(request, 'contatos/adicionarcontato.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    telefone = request.POST.get('telefone')
    email = request.POST.get('email')
    categoria = request.POST.get('categoria')
        
    contato = Contato.objects.create(nome=nome, sobrenome=sobrenome, telefone=telefone, email=email or None, categoria_id=categoria)
    contato.save()
    return render(request, 'contatos/adicionarcontato.html')



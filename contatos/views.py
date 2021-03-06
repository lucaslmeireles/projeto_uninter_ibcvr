from django.core.validators import validate_email
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from .models import Categoria, Contato
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.mail import EmailMessage
from agenda import settings


# Create your views here.
def paginicio(request):
    #cria a pagina inicial
    return render(request, 'contatos/inicio.html')
def sobre(request):
    #cria a pag sobre
    return render(request, 'contatos/inicio.html')

class PagInicialAgenda(LoginRequiredMixin, ListView):
    #cria a lista da agenda
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
    #TODO Pesquisar como colocar o numero de contatos cadastrados, e usuarios
    # testar essa solucao 
    # i=0
    # for contato in Contato.objects.all():
    #     i += 1
    # for user in User.objects.all():
    #     i += 1



    if len(telefone)< 9:
        messages.error(
            request,
            'Número de telefone inválido'
        )
        return render(request, 'contatos/adicionarcontato.html')
    try:
        validate_email(email)
    except:
        messages.error(
        request,
        'Email inválido'
        )
        return render(request, 'contatos/adicionarcontato.html')

    contato = Contato.objects.create(nome=nome, sobrenome=sobrenome, telefone=telefone, email=email or None, categoria_id=categoria)
    contato.save()
    messages.success(
            request,
            'Contato adicionado com sucesso'
        )


    return render(request, 'contatos/adicionarcontato.html')

def enviaemail(request):
    if request.method != 'POST':
        return render(request, 'contatos/adicionarcontato.html')

    email_contato = []
    nao_tem_email = []
    for contato in Contato.objects.all():
        if contato.email:
            email_contato.append(contato.email)
        else:
            nao_tem_email.append(contato.nome)
    i = 0
    for sem_email in nao_tem_email:
        i += 1

    assunto = request.POST.get('assunto')
    mensagem = request.POST.get('mensagem')
    destinatarios = request.POST.get('destinatarios')
    arquivos = request.FILES.get('arquivos')

    if not assunto or not mensagem:
        messages.error(
            request,
            'Seu email é invalido'
        )
        return render(request, 'contatos/adicionarcontato.html')
    
    #TODO AQUI TEM MAIS COISAS COMO UMA VERIFICACAO, TBM PRECISA PREVINIR BADHEAD
    # E LOGICO TESTAR TUDO
    email = EmailMessage(
        subject=assunto,
        body=mensagem,
        from_email=settings.EMAIL_HOST_USER,
        to=['lluciomeireles@gmail.com', 'llmeireles0015@gmail.com', 'acrmeireles@hotmail.com', 'mnlmeireles@hotmail.com']
    )
        


    if arquivos:
        email.attach_file(arquivos)
    
    email.send()
    messages.success(request, 'Email enviado')

    #TODO  COMO FAZER ESSE NEGOCIO EXIBiR UM VALOR BONITINHO DE CADA VEZ
    messages.warning(
        request,
        'Não foi possivel enviar a mensagem para todo os contatos'
        f'Contatos sem email {sem_email}'
    )



    return render(request, 'contatos/adicionarcontato.html')



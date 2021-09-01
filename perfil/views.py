from django.shortcuts import redirect, render
from django.core.validators import validate_email
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

def cadastro(request):
    if request.method != 'POST':
        return render(request, 'perfil/cadastro.html')
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(
            request,
            'Nenhum campo pode estar vazio'
        )
        return render(request, 'perfil/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(
            request,
            'Email invalido'
        )
        return render(request, 'perfil/cadastro.html')
    if len(senha) < 6:
        messages.error(
            request,
            'Senha precisa ter mais de 6 caracteres'
        )
        return render(request, 'perfil/cadastro.html')

    if senha != senha2:
        messages.error(
            request,
            'As senhas nao coincidem'
        )
        return render(request, 'perfil/cadastro.html')

    if len(usuario) <6:
        messages.error(
            request,
            'O usuario deve ter mais de 6 caracteres'
        )
        return render(request, 'perfil/cadastro.html')
    if User.objects.filter(username=usuario).exists():
        messages.error(
            request,
            'O usuario já existe'
        )
        return render(request, 'perfil/cadastro.html')
    if User.objects.filter(email=email).exists():
        messages.error(
            request,
            'O email já tem cadastro'
        )
        return render(request, 'perfil/cadastro.html')

    messages.success(
            request,
            'Usuario cadastrado com sucesso, faça login'
        )
    user = User.objects.create_user(username=usuario, email=email, password=senha, 
    first_name=nome, last_name=sobrenome)
    user.save()
    return redirect('login')

def login(request):
    if request.method != 'POST':
        return render(request, 'perfil/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(
            request,
            'Usuario ou senha invalidos'
        )
        return render(request, 'perfil/login.html')
    else:
        auth.login(request, user)
        return redirect('index')

def logout(request):
    
    auth.logout(request)
    
    return redirect('login')





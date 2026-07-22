from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroUsuarioForm

def dashboard(request):
    """
    View responsável por renderizar a página do dashboard do usuário.
    """
    return render(request, 'gestao_treinos/dashboard.html')

def registrar_usuario(request):
    """
    View responsável pelo auto-cadastro (inscrição) de novos usuários no sistema.
    """
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Faz o login automático do usuário logo após o cadastro
            login(request, user)
            # Redireciona para o dashboard após se inscrever
            return redirect('gestao_treinos:dashboard')
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'gestao_treinos/registro.html', {'form': form})
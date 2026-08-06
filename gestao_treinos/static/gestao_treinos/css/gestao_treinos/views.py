def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # cria perfil já com tipo "aluno"
            PerfilUsuario.objects.create(user=user, tipo="aluno")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def aluno_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard_aluno")  # rota que vamos criar
        else:
            return render(request, "login.html", {"error": "Usuário ou senha inválidos"})
    return render(request, "login.html")


@login_required
def dashboard_aluno(request):
    return render(request, "dashboard_aluno.html")

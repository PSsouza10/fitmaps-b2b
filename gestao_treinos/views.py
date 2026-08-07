from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Prescricao, Treino

# Página inicial (home)
def home(request):
    return render(request, "gestao_treinos/home.html")

# Login do aluno
def aluno_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard_aluno")
        else:
            return render(
                request,
                "gestao_treinos/login.html",
                {"error": "Usuário ou senha inválidos"}
            )
    return render(request, "gestao_treinos/login.html")

# Dashboard do aluno
@login_required
def dashboard_aluno(request):
    if request.method == "POST":
        data_treino = request.POST.get("data_treino")
        distancia_km = request.POST.get("distancia_km")
        tempo_minutos = request.POST.get("tempo_minutos")

        Treino.objects.create(
            data_treino=data_treino,
            distancia_km=distancia_km,
            tempo_minutos=tempo_minutos,
            aluno=request.user  # treino ligado ao usuário logado
        )
        return redirect("dashboard_aluno")

    prescricoes = Prescricao.objects.all()
    treinos = Treino.objects.filter(aluno=request.user)  # só treinos do aluno logado
    return render(request, "gestao_treinos/dashboard.html", {
        "prescricoes": prescricoes,
        "treinos": treinos
    })

# Logout do aluno
def aluno_logout(request):
    logout(request)
    return redirect("aluno_login")

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from gestao_treinos import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dashboard/aluno/", views.dashboard_aluno, name="dashboard_aluno"),
    path("login/aluno/", LoginView.as_view(template_name="login.html"), name="aluno_login"),

    # ✅ Usa o NOME da URL em vez de caminho absoluto
    path("logout/", LogoutView.as_view(next_page="aluno_login"), name="logout"),

    # ✅ Redireciona a raiz "/" para o login do aluno
    path("", lambda request: redirect("aluno_login"), name="home"),
]
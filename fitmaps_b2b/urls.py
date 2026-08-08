from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from gestao_treinos import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dashboard/aluno/", views.dashboard_aluno, name="dashboard_aluno"),
    path("login/aluno/", LoginView.as_view(template_name="login.html"), name="aluno_login"),

    # ✅ Usa a view customizada de logout (aceita GET, redireciona para login)
    path("logout/", views.aluno_logout, name="logout"),

    # ✅ Redireciona a raiz "/" para o login do aluno
    path("", lambda request: redirect("aluno_login"), name="home"),
]
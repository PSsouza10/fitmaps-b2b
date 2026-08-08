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

    # ✅ Redireciona a raiz "/" from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from gestao_treinos import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Dashboard do aluno
    path("dashboard/aluno/", views.dashboard_aluno, name="dashboard_aluno"),

    # ✅ Usa a view customizada de login
    path("login/aluno/", views.aluno_login, name="aluno_login"),

    # ✅ Logout do aluno
    path("logout/", views.aluno_logout, name="aluno_logout"),

    # ✅ Redireciona a raiz "/" para o login do aluno
    path("", lambda request: redirect("aluno_login"), name="home"),
]
para o login do aluno
    path("", views.home, name="home"),

]
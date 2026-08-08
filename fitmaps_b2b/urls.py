from django.contrib import admin
from django.urls import path
from gestao_treinos import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Dashboard do aluno
    path("dashboard/aluno/", views.dashboard_aluno, name="dashboard_aluno"),

    # Login e Logout do aluno
    path("login/aluno/", views.aluno_login, name="aluno_login"),
    path("logout/", views.aluno_logout, name="aluno_logout"),

    # Redireciona a raiz "/" para o login do aluno
    path("", lambda request: redirect("aluno_login"), name="home"),
]
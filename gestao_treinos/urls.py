from django.urls import path
from . import views

urlpatterns = [
    # Página inicial
    path("", views.home, name="home"),

    # Login do aluno
    path("login/aluno/", views.aluno_login, name="aluno_login"),

    # Dashboard do aluno
    path("dashboard/aluno/", views.dashboard_aluno, name="dashboard_aluno"),

    # Logout do aluno
    path("logout/", views.aluno_logout, name="aluno_logout"),
]

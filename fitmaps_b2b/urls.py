from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from gestao_treinos import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dashboard/aluno/", views.dashboard_aluno, name="dashboard_aluno"),
    path("login/aluno/", LoginView.as_view(template_name="login.html"), name="aluno_login"),
    path("logout/", LogoutView.as_view(next_page="/admin/login/"), name="logout"),
    path("", include("gestao_treinos.urls")),  # se o app tiver urls próprias
]

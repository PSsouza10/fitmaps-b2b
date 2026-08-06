from django.contrib import admin
from django.urls import path
from gestao_treinos import views

urlpatterns = [
    path("admin/", admin.site.urls),  # rota do painel admin
    path("dashboard/aluno/", views.dashboard_aluno, name="dashboard_aluno"),  # rota do dashboard
]

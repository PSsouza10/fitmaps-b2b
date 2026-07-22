from django.urls import path
from . import views

app_name = 'gestao_treinos'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cadastro/', views.registrar_usuario, name='cadastro'),
]
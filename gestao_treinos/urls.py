from django.urls import path
from . import views

app_name = 'gestao_treinos'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cadastro/', views.registrar_usuario, name='cadastro'),
    path('novo-treino/', views.novo_treino, name='novo_treino'), # Adicione esta linha se a sua view se chamar novo_treino
]
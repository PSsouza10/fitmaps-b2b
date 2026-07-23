from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from gestao_treinos import views  # Certifique-se de importar as views do seu app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/dashboard/', permanent=False)), # Redireciona a raiz para o dashboard
    path('dashboard/', views.dashboard, name='dashboard'),             # Substitua 'dashboard' pela sua view real
    path('cadastro/', views.cadastro, name='cadastro'),                # Substitua 'cadastro' pela sua view real
]
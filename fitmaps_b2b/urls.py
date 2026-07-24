from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: HttpResponseRedirect('/dashboard/')),  # Redireciona a raiz para o dashboard
    path('', include('gestao_treinos.urls')),                       # Delega todas as rotas para o app gestao_treinos
]
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # Adiciona login, logout, etc.
    path('', lambda request: HttpResponseRedirect('/dashboard/')),  
    path('', include('gestao_treinos.urls')),                       
]
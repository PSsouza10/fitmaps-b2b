from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.painel_atleta, name="painel_atleta"),
]

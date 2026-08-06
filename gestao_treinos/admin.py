from django.contrib import admin
from .models import Prescricao, Treino


@admin.register(Prescricao)
class PrescricaoAdmin(admin.ModelAdmin):
    list_display = ("id", "detalhes")  # mostra ID e detalhes
    search_fields = ("detalhes",)      # permite buscar por texto


@admin.register(Treino)
class TreinoAdmin(admin.ModelAdmin):
    list_display = ("id", "aluno", "data_treino", "distancia_km", "tempo_minutos", "prescricao")
    list_filter = ("data_treino", "aluno")  # filtros laterais
    search_fields = ("aluno__username", "prescricao__detalhes")  # busca por aluno ou prescrição

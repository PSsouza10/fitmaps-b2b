from django.contrib import admin
from .models import PerfilUsuario, Treino, PrescricaoTreino

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'tipo')
    list_filter = ('tipo',)
    search_fields = ('user__username', 'user__email')

@admin.register(Treino)
class TreinoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data_treino', 'distancia_km', 'tempo_minutos', 'ritmo_medio', 'calorias', 'zona_predominante')
    list_filter = ('zona_predominante', 'data_treino', 'usuario')
    search_fields = ('usuario__username',)

@admin.register(PrescricaoTreino)
class PrescricaoTreinoAdmin(admin.ModelAdmin):
    list_display = ('atleta', 'profissional', 'data_limite', 'concluido')
    list_filter = ('concluido', 'data_limite')
    search_fields = ('atleta__username', 'profissional__username', 'descricao_meta')

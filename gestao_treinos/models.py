from django.db import models
from django.contrib.auth.models import User


# Prescrição de treino (ex: instruções do professor)
class Prescricao(models.Model):
    detalhes = models.TextField(default="Sem detalhes")  # valor padrão

    def __str__(self):
        return self.detalhes[:50]  # mostra os primeiros 50 caracteres


# Registro de treino feito pelo aluno
class Treino(models.Model):
    aluno = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # usuário ID 1 como padrão
    prescricao = models.ForeignKey(Prescricao, on_delete=models.SET_NULL, null=True, blank=True)  # vínculo opcional
    data_treino = models.DateField(auto_now_add=True)  # salva a data automaticamente
    distancia_km = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    tempo_minutos = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.aluno.username} - {self.data_treino}"

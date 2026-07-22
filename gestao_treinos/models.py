from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    TIPO_CHOICES = (
        ('atleta', 'Atleta / Aluno'),
        ('treinador', 'Treinador / Educador'),
        ('medico', 'Médico / Profissional de Saúde'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='atleta')

    def __str__(self):
        return f"{self.user.username} ({self.get_tipo_display()})"

class Treino(models.Model):
    ZONA_CHOICES = (
        ('Z1', 'Zona 1 - Recuperação'),
        ('Z2', 'Zona 2 - Aeróbico / Base'),
        ('Z3', 'Zona 3 - Limiar / Tempo'),
        ('Z4', 'Zona 4 - VO2 Máximo'),
        ('Z5', 'Zona 5 - Anaeróbico'),
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    data_treino = models.DateField(verbose_name="Data do Treino")
    distancia_km = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Distância (km)")
    tempo_minutos = models.IntegerField(verbose_name="Tempo (minutos)")
    ritmo_medio = models.CharField(max_length=10, blank=True, null=True, verbose_name="Ritmo Médio")
    calorias = models.IntegerField(default=0, verbose_name="Calorias (kcal)")
    zona_predominante = models.CharField(max_length=2, choices=ZONA_CHOICES, blank=True, null=True, verbose_name="Zona Cardíaca Predominante")

    def __str__(self):
        return f"Treino de {self.usuario.username} em {self.data_treino}"

class PrescricaoTreino(models.Model):
    profissional = models.ForeignKey(User, on_delete=models.CASCADE, related_name="prescricoes_feitas", verbose_name="Profissional")
    atleta = models.ForeignKey(User, on_delete=models.CASCADE, related_name="prescricoes_recebidas", verbose_name="Atleta")
    descricao_meta = models.TextField(verbose_name="Descrição da Meta / Prescrição")
    data_limite = models.DateField(verbose_name="Data Limite")
    concluido = models.BooleanField(default=False, verbose_name="Concluído")

    def __str__(self):
        return f"Prescrição para {self.atleta.username} por {self.profissional.username}"

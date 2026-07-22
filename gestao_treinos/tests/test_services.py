from django.test import TestCase
from django.contrib.auth.models import User
from gestao_treinos.services.treino_service import TreinoService
from gestao_treinos.exceptions import TreinoInvalidoError
from datetime import date

class TreinoServiceTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='atleta_teste', password='123')

    def testar_criacao_treino_valido(self):
        dados = {
            'data_treino': date.today(),
            'distancia_km': 10.5,
            'tempo_minutos': 50,
            'zona_predominante': 'Z2'
        }
        treino = TreinoService.processar_novo_treino(self.user, dados)
        self.assertEqual(treino.distancia_km, 10.5)

    def testar_falha_distancia_negativa(self):
        dados = {
            'data_treino': date.today(),
            'distancia_km': -5.0,
            'tempo_minutos': 30
        }
        with self.assertRaises(TreinoInvalidoError):
            TreinoService.processar_novo_treino(self.user, dados)

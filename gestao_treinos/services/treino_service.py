from django.contrib.auth.models import User

from ..repositories.treino_repository import (
    TreinoRepository,
    PrescricaoRepository,
    PerfilRepository,
)
from ..exceptions import TreinoInvalidoError


class TreinoService:
    def __init__(
        self,
        treino_repo: TreinoRepository = None,
        prescricao_repo: PrescricaoRepository = None,
        perfil_repo: PerfilRepository = None,
    ):
        # Injeção de dependência: em testes, você pode passar mocks aqui
        # sem precisar tocar em um banco de dados real[cite: 4].
        self.treino_repo = treino_repo or TreinoRepository()
        self.prescricao_repo = prescricao_repo or PrescricaoRepository()
        self.perfil_repo = perfil_repo or PerfilRepository()

    def processar_novo_treino(self, usuario: User, dados_treino: dict):
        # O Service foca puramente nas regras de negócio da aplicação[cite: 4]
        if dados_treino.get("distancia_km", 0) < 0:
            raise TreinoInvalidoError(
                "A distância do treino não pode ser negativa."
            )

        if dados_treino.get("tempo_minutos", 0) <= 0:
            raise TreinoInvalidoError(
                "O tempo do treino deve ser maior que zero."
            )

        return self.treino_repo.criar_treino(usuario, dados_treino)

    def montar_contexto_dashboard(self, usuario: User) -> dict:
        # Centraliza a montagem do dicionário de dados que a view vai renderizar[cite: 4]
        return {
            "treinos": self.treino_repo.listar_por_usuario(usuario),
            "prescricoes": self.prescricao_repo.listar_pendentes(usuario),
            "perfil": self.perfil_repo.obter_ou_criar(usuario),
        }

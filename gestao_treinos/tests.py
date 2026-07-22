from unittest.mock import Mock
import pytest
from django.contrib.auth.models import User
from gestao_treinos.services.treino_service import TreinoService
from gestao_treinos.repositories.treino_repository import TreinoRepository
from gestao_treinos.exceptions import TreinoInvalidoError


def test_treino_negativo_lanca_erro():
    # Arrange (Prepara o usuário e o mock do repositório)
    usuario = User(username="atleta_teste")
    mock_repo = Mock(spec=TreinoRepository)
    service = TreinoService(treino_repo=mock_repo)
    
    # Act & Assert (Garante que a exceção é lançada e o repo NÃO tenta salvar no banco)
    with pytest.raises(TreinoInvalidoError):
        service.processar_novo_treino(usuario, {"distancia_km": -5, "tempo_minutos": 30})
        
    mock_repo.criar_treino.assert_not_called()

from django.db import transaction
from django.contrib.auth.models import User
from ..models import Treino, PrescricaoTreino, PerfilUsuario


class TreinoRepository:
    """
    Isola as consultas de treinos e garante transações atômicas na criação.
    """
    def listar_por_usuario(self, usuario: User):
        return (
            Treino.objects
            .filter(usuario=usuario)
            .select_related("usuario")
            .order_by("-data_treino")
        )

    def criar_treino(self, usuario: User, dados: dict) -> Treino:
        with transaction.atomic():
            return Treino.objects.create(usuario=usuario, **dados)


class PrescricaoRepository:
    def listar_pendentes(self, usuario: User):
        return (
            PrescricaoTreino.objects
            .filter(atleta=usuario, concluido=False)
            .select_related("atleta")
        )


class PerfilRepository:
    def obter_ou_criar(self, usuario: User) -> PerfilUsuario:
        perfil, _ = PerfilUsuario.objects.get_or_create(user=usuario)
        return perfil

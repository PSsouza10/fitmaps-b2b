from django.core.exceptions import ValidationError

class TreinoInvalidoError(ValidationError):
    """Exceção disparada quando os dados do treino violam as regras de negócio."""
    pass

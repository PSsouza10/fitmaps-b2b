# Cria e ativa o ambiente virtual Python
python -m venv venv
venv\Scripts\activate  # No Windows
# source venv/bin/activate  # No Mac/Linux

# Instala o framework robusto e o conector do banco de dados
pip install django psycopg2-binary djangorestframework

# Inicializa o projeto B2B e o aplicativo principal
django-admin startproject fitmaps_b2b .
django-admin startapp gestao_treinos
import uuid
from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    treinador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alunos')
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome

class ExercicioCatalogo(models.Model):
    # Catálogo imutável gerenciado por você (Desenvolvedor)
    nome = models.CharField(max_length=100)
    grupo_muscular = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} - {self.grupo_muscular}"

class FichaTreino(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='fichas')
    nome_ficha = models.CharField(max_length=50) # Ex: Treino A - Peito
    data_criacao = models.DateTimeField(auto_now_add=True)

    def clonar_para_aluno(self, novo_aluno):
        """
        Método robusto para o sistema B2B: Clona a ficha inteira e todos 
        os seus exercícios detalhados para um novo aluno em milissegundos.
        """
        nova_ficha = FichaTreino.objects.create(
            aluno=novo_aluno,
            nome_ficha=self.nome_ficha
        )
        exercicios = self.itens_treino.all()
        novos_itens = [
            ItemFicha(
                ficha=nova_ficha,
                exercicio=item.exercicio,
                series=item.series,
                repeticoes=item.repeticoes,
                descanso_segundos=item.descanso_segundos
            ) for item in exercicios
        ]
        ItemFicha.objects.bulk_create(novos_itens) # Salva tudo de uma vez no banco
        return nova_ficha

class ItemFicha(models.Model):
    ficha = models.ForeignKey(FichaTreino, on_delete=models.CASCADE, related_name='itens_treino')
    exercicio = models.ForeignKey(ExercicioCatalogo, on_delete=models.PROTECT)
    series = models.IntegerField()
    repeticoes = models.IntegerField()
    descanso_segundos = models.IntegerField(default=60)
    ordem_execucao = models.IntegerField(default=1) # Para garantir a sequência correta

    class Meta:
        ordering = ['ordem_execucao']$env:Path = "C:\Users\Jorge\.local\bin;$env:Path"
uv venv
.\.venv\Scripts\activate
uv pip install django psycopg2-binary djangorestframework
django-admin startproject fitmaps_b2b .
django-admin startapp gestao_treinos

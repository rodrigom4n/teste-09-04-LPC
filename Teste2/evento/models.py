from django.db import models

# Create your models here.

class Avaliador(models.Model):
	nome = models.CharField(max_length=150)
	email = models.CharField(max_length=100)

	def __str__(self):
		return self.nome

class Autor(models.Model):
	nome = models.CharField(max_length=150)
	email = models.CharField(max_length=100)

	def __str__(self):
		return self.nome

class Nota(models.Model):
    qualidade_tecnica = models.CharField(max_length=150)
    inovacao = models.CharField(max_length=100)
    resultados = models.CharField(max_length=100)
    metodologia = models.CharField(max_length=100)
    adequacao = models.CharField(max_length=100)

    def __str__(self):
        return self.qualidade_tecnica

class Avaliacao(models.Model):
    media = models.CharField(max_length=100)
    def __str__(self):
        return self.media

class Artigo(models.Model):
    titulo = models.CharField(max_length=150)
    avaliacao = models.ForeignKey(Avaliacao, related_name="Avaliacoes", null=True, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo

class ArtigoAutor(models.Model):
    autor = models.ForeignKey(Autor, related_name="Autores", null=True, blank=False, on_delete=models.CASCADE)
    artigo = models.ForeignKey(Autor, related_name="Artigos", null=True, blank=False, on_delete=models.CASCADE)

class AvaliacaoAvaliador(models.Model):
    avaliador = models.ForeignKey(Avaliador, related_name="Avaliador", null=True, blank=False, on_delete=models.CASCADE)
    avaliacao = models.ForeignKey(Avaliacao, related_name="Avaliacao", null=True, blank=False, on_delete=models.CASCADE)

class AvaliacaoNota(models.Model):
    nota = models.ForeignKey(Nota, related_name="NotasAv", null=True, blank=False, on_delete=models.CASCADE)
    avaliacao = models.ForeignKey(Avaliacao, related_name="AvaliacaoAv", null=True, blank=False, on_delete=models.CASCADE)
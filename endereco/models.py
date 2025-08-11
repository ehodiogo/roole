from django.db import models


class Pais(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Estado(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=11)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.pais.nome}"


class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.estado.uf}"


class Endereco(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return f"{self.nome} - {self.cidade.nome}"

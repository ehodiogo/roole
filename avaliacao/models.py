from django.db import models

class Avaliacao(models.Model):
    nota = models.FloatField()
    role = models.ForeignKey('role.Role', on_delete=models.PROTECT)
    descricao = models.TextField()
    foto = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.role.nome} - {self.descricao} - {self.nota}"
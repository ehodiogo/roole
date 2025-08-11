from django.db import models


class Local(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.ForeignKey("endereco.Endereco", on_delete=models.CASCADE)
    logo = models.ImageField(upload_to="logo", null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.endereco.cidade.nome}"

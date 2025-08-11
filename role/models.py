from django.db import models

class Role(models.Model):
    nome = models.CharField(max_length=120)
    local = models.ForeignKey('local.Local', on_delete=models.CASCADE)
    data = models.DateTimeField(null=True, blank=True)
    foto = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.local.nome} - {self.data.strftime('%d/%m/%Y')}"
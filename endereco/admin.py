from django.contrib import admin
from .models import Pais,Cidade,Estado, Endereco

admin.site.register(Pais)
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Endereco)

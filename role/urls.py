from django.urls import path
from .views import home, roles, roles_perto, roles_por_cidade

urlpatterns = [
    path("", home),
    path("roles/", roles),
    path("roles-perto/", roles_perto),
    path("roles-cidade/", roles_por_cidade),
]

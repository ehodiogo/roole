from django.shortcuts import render
from local.models import Local
from django.http import JsonResponse
import math
from role.models import Role


def home(request):
    return render(request, "home.html")


def distancia_km(lat1, lon1, lat2, lon2):
    R = 6371  # Raio da Terra em km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


def roles_perto(request):
    try:
        lat = float(request.GET.get("lat"))
        lon = float(request.GET.get("lon"))
    except (TypeError, ValueError):
        return JsonResponse({"error": "Coordenadas inválidas"}, status=400)

    print("Latitude: ", lat)
    print("Longitude: ", lon)

    limite_km = 10
    eventos_proximos = []

    for role in Role.objects.all():
        dist = distancia_km(lat, lon, role.local.endereco.lat, role.local.endereco.lng)
        if dist <= limite_km:
            eventos_proximos.append(
                {
                    "nome": role.nome,
                    "distancia_km": round(dist, 2),
                    "descricao": role.local.nome,
                }
            )

    return JsonResponse({"roles": eventos_proximos})


def roles_por_cidade(request):
    cidade = request.GET.get("cidade", "").strip().lower()
    if not cidade:
        return JsonResponse({"error": "Cidade não informada"}, status=400)

    eventos = Role.objects.filter(local__endereco__cidade__nome__icontains=cidade)

    lista = [
        {
            "nome": r.nome,
            "descricao": r.local.nome,
            "cidade": r.local.endereco.cidade.nome,
        }
        for r in eventos
    ]

    return JsonResponse({"roles": lista})


def roles(request):
    return render(request, "roles.html")


def locais(request):
    return render(request, "locais.html")

from .models import videojuego
from rest_framework import viewsets
from rest_framework.response import Response
from .serial import videojuegoserializer

# conjunto de vistas para el CRUD del modelo
class videojuegoviewsets(viewsets.ModelViewSet):
    queryset = videojuego.objects.all().order_by('-genero')
    serializer_class = videojuegoserializer

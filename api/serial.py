from rest_framework import serializers

#se importa el modelo
from .models import videojuego

#se crea el serializador
class videojuegoserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = videojuego
        fields = ['nombre', 'pais_origen', 'año', 'genero', 'precio']

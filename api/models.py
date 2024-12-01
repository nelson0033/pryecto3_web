from django.db import models

# Create your models here.
class videojuego(models.Model):
    """
    Modelo que representa la estructura de datos
    de un regustro correspondiente a un videojuego 
    en base de datos
    """
    nombre = models.CharField(max_length=50)
    pais_origen = models.CharField(max_length=20)
    año = models.IntegerField()
    genero = models.CharField(max_length=20)
    precio = models.IntegerField()
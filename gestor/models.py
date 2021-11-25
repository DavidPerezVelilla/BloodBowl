from typing import Generic
from django.db import models
from django.contrib.messages.views import SuccessMessageMixin


# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField('Nombre', 
        max_length=100)

    raza = models.ForeignKey('Razas', on_delete=models.SET_NULL,
        null=True, blank=True)
    

    def __str__(self):
        return self.nombre
    
    desc = models.CharField('Descripcion', max_length=5000, null=True)

    img = models.CharField('Imagen', max_length=500, null=True)

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
    
class Razas(models.Model):
    nombre = models.CharField('Nombre', max_length=250)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Raza'
        verbose_name_plural = 'Razas'

class Jugador (models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    equipo = models.ForeignKey('Equipo',on_delete=models.SET_NULL,
    null=True, blank=True)
    coste = models.CharField('Coste', max_length=100)
    movimiento = models.CharField('Movimiento',max_length=100)
    fuerza = models.CharField('Fuerza', max_length=100)
    agilidad = models.CharField('Agilidad', max_length=100)
    pase = models.CharField('Pase', max_length=100)
    armadura = models.CharField('Armadura', max_length=100)
    habilidades = models.CharField('Habilidades', max_length=200)
    class Meta:
            verbose_name = 'Jugador'
            verbose_name_plural = 'Jugadores'

    def __str__(self):
        return self.nombre



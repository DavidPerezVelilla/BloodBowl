from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField('Nombre', 
        max_length=100)
    estadio = models.CharField('Estadio', 
        max_length=100)
    raza = models.ForeignKey('Raza', on_delete=models.SET_NULL,
        null=False, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
    
class Razas(models.Model):
    nombre = models.CharField('Nombre', max_length=250)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Raza'

class Jugador (models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    apellido = models.CharField('Apellido',max_length=100)
    equipo = models.ForeignKey('Equipo',on_delete=models.SET_NULL,
    null=True, blank=True)

    def __str__(self):
        return self.nombre
from django.contrib import admin

# Register your models here.
from .models import Equipo, Jugador, Razas 
@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'raza']
    list_filter = ['raza']

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'equipo', 
        'coste', 'movimiento', 'fuerza', 'agilidad', 'pase', 'armadura', 'habilidades']
 

@admin.register(Razas)
class RazaAdmin(admin.ModelAdmin):
    pass

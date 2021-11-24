from os import name
from django.urls import include, path
from gestor.views import EquipoDetailView, EquiposListView, SearchResultsListView, subir_archivo, tiendas



urlpatterns = [
   path("tiendas", tiendas,name='tiendas'),
   path("subir-archivo", subir_archivo, name='subir_archivo'),
   path('buscarequipos/', SearchResultsListView.as_view(), name="buscar" ),
   path('equipo_list', EquiposListView.as_view(), name='listado'),
   path('detalle_equipo/<int:pk>', EquipoDetailView.as_view(), name="detalle_equipo")
]
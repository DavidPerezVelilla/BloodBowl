from typing import Generic
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls.base import is_valid_path
from django.views import generic
from django.urls import resolve, reverse
from django.views.generic import ListView, CreateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
import os #esto es para construir rutas con os.path
from django.conf import settings
from gestor.models import Equipo, Jugador
from gestor.forms import EquipoForm 


# Create your views here.
def indice(request):
    '''
    Página inicial de nuestra web
    '''
    datos = {'autor': 'David Perez'}
    #ejmplo sesiones
    visitas = request.session.get('visitas', 0)
    request.session['visitas']= visitas +1
    datos['visitas'] = visitas
    # últimos 5 libros del catálogo

     
    return render(request, 'index.html',
        context=datos)

def tiendas(request):
    return render(request, 'tiendas.html')

def subir_archivo (request):
    #Si estamos dentro de un post haremos algo (post es que nos envian algo)
    if request.method == 'POST':
        #Procesar archivo
        #le dirermos que nos construya una ruta 
        # del media root al archivo que hemos subido
        nombre = request.FILES["archivo"].name
        save_path = os.path.join(settings.MEDIA_ROOT, nombre)

        #crear archivo con fragmentos
        with open(save_path, "wb") as output_file:
            for chunk in request.FILES["archivo"].chunks():
                output_file.write(chunk)
        messages.add_message(request,messages.SUCCESS, 'Archivo subido')
        
        return render(request, 'subir-archivo.html')

    #si solo es un get mostrara el formulario 
    else:
        return render(request, 'subir-archivo.html') 

class SearchResultsListView(ListView):
    model = Equipo
    context_object_name = 'equipos'
    template_name = 'search_results.html'  # No usará la plantilla estándar del ListView
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        if query:
            return Equipo.objects.filter(nombre__icontains=query)
        return []  # cuando entramos a buscar o si no se introduce nada  


class EquiposListView(generic.ListView):
    
    model = Equipo
    paginate_by = 6

class EquipoDetailView(generic.DetailView):
   
    model = Equipo

class JugadoresDetailView(generic.DetailView):

    model = Jugador

@login_required
def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            # Mensaje para informar éxito redirección
            messages.add_message(request, 
                messages.SUCCESS, 
                'Equipo creado.')
            return redirect('/')
    else:
        form = EquipoForm()
    datos = {'form': EquipoForm()}
    return render(request, 'crear_equipo.html', 
        context=datos)
    
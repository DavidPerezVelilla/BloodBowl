from django.shortcuts import render

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
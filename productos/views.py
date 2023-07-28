from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from productos.models import *

def productos_list(request):
        data = {
            'title': 'Stock de Inventario',
            'producto': Producto.object.all()
        }
        return render(request, 'templates/inventario.html', data)

class ProductosListView(ListView):
    model = Producto
    template_name = 'inventario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Stock en Inventario'
        context['object_list'] = Producto.objects.all()
        return context
    

    
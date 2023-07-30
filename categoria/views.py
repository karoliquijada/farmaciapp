from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from productos.models import *

def categoria_list(request):
        data = {
            'title': 'Categoria',
            'producto': Categoria_Producto.object.all()
        }
        return render(request, 'templates/categoria.html', data)

class CategoriaListView(ListView):
    model = Categoria_Producto
    template_name = 'categoria.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Categoria'
        context['categoria_object_list'] = Categoria_Producto.objects.all()
        context['subcategoria1_object_list'] = MN_Subcategoria_Producto.objects.filter(categoria='Vitaminas y Productos Naturales')
        context['subcategoria2_object_list'] = MN_Subcategoria_Producto.objects.filter(categoria='Dolor General')
        context['subcategoria3_object_list'] = MN_Subcategoria_Producto.objects.filter(categoria='Salud Respiratoria y Gripe')
        return context
    
    

    
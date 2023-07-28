from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from productos.models import *

class ProductosListView(ListView):
    model = Producto
    template_name = 'inventario.html'
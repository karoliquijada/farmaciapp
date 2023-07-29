from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.views.generic import ListView
from compras.models import *
from .forms import CompraForm
from django.urls import reverse_lazy

class CompraView(CreateView):
    model = Compra
    template_name = 'compras/agregar_compra.html'
    form_class = CompraForm
    success_url = reverse_lazy('historial_compra')
class ComprasHistorialListView(ListView):
    model = Compra
    template_name = 'compras/historial_compra.html'
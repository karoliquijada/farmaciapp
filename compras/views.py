from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.views.generic import ListView
from compras.models import *
from productos.models import Producto
from proveedores.models import Proveedor
from .forms import CompraForm
from django.urls import reverse_lazy

class CompraView(CreateView):
    model = Compra
    template_name = 'compras/agregar_compra.html'
    form_class = CompraForm
    success_url = reverse_lazy('historial')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proveedores'] = Proveedor.objects.all()
        context['productos'] = Producto.objects.all()  # Aquí agregas tu variable con su valor
        return context
    
class CompraDeleteView(DeleteView):
    model = Compra
    template_name = 'compras/eliminar_compras.html'
    success_url = reverse_lazy('historial')  # Redirige a la vista del historial de compras después de eliminar

    def get_success_url(self):
        return self.success_url

class CompraUpdateView(UpdateView):
    model = Compra
    template_name = 'compras/editar_compra.html'
    form_class = CompraForm
    success_url = reverse_lazy('historial')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proveedores'] = Proveedor.objects.all()
        context['productos'] = Producto.objects.all()
        return context
    
class ComprasHistorialListView(ListView):
    model = Compra
    template_name = 'compras/historial_compra.html'
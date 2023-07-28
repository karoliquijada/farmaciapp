from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from ventas.models import *

class VentaListView(ListView):
    model = Metodo_de_pago
    template_name = 'index.html',
from django.shortcuts import render
from django.http import HttpResponse
from reportes.models import *
from django.views.generic import ListView

class ReporteListView(ListView):
    model = Factura
    template_name = 'reporte.html'
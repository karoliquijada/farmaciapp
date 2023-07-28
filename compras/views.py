from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from compras.models import *

class ComprasListView(ListView):
    model = Compra
    template_name = 'compra.html'
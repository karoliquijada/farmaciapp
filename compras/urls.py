from django.urls import path
from compras.views import *
from . import views

urlpatterns = [
    path("compra/", CompraView.as_view(), name="compra"),
    path("historial/", ComprasHistorialListView.as_view(), name="historial"),
]
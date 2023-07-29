from django.urls import path
from compras.views import *
from . import views

urlpatterns = [
    path("compra/", CompraView.as_view(), name="compra"),
    path('compra/<int:pk>/eliminar/', CompraDeleteView.as_view(), name='eliminar_compra'),
    path('compra/<int:pk>/editar/', CompraUpdateView.as_view(), name='editar_compra'),
    path("historial/", ComprasHistorialListView.as_view(), name="historial"),
]
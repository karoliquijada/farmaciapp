from django.urls import path

from . import views
from ventas.views import *

urlpatterns = [
    path("venta/", VentaListView.as_view(), name="venta"),
]
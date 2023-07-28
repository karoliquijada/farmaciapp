from django.urls import path

from . import views
from productos.views import *

urlpatterns = [
    path("inventario/", ProductosListView.as_view(), name="inventario"),
]
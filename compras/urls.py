from django.urls import path
from compras.views import *
from . import views

urlpatterns = [
    path("compra/", ComprasListView.as_view(), name="compra"),
]
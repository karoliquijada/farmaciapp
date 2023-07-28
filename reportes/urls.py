from django.urls import path

from . import views
from reportes.views import *

urlpatterns = [
    path("reporte/", ReporteListView.as_view(), name="reporte"),
]

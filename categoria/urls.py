from django.urls import path

from . import views
from categoria.views import *

urlpatterns = [
    path("categoria/", CategoriaListView.as_view(), name="categoria"),
]
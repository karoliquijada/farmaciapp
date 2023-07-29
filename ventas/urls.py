from django.urls import path

from . import views

urlpatterns = [
    
    path("clientes", views.clientesv, name="SubMenuCV"),
    path("anadir_cliente", views.anadircv, name="AddCliente"),
    path("editar_cliente", views.editarcv, name="EditCliente"),
    path("borrar_cliente", views.borrarcv, name="DeleteCliente"),
    path("productos", views.productosv, name="SubMenuCV"),
    path("anadir_producto", views.anadirpv, name="AddProducto"),
    path("editar_producto", views.editarpv, name="EditProducto"),
    path("borrar_producto", views.borrarpv, name="DeleteProducto"),
    path('',views.add_ventas.as_view(), name='AddVenta'),
    path('export/', views.export_pdf_view, name="ExportPDF" ),
    path('export/<id>/<iva>', views.export_pdf_view, name="ExportPDF" ),
]
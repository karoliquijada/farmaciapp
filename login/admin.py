from django.contrib import admin
from compras.models import Compra
from proveedores.models import Proveedor
from productos.models import Producto
# Register your models here.

admin.site.register(Compra)
admin.site.register(Producto)
admin.site.register(Proveedor)

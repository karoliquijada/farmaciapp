from django.contrib import admin
from compras.models import Compra
from proveedores.models import Proveedor
from productos.models import Producto
from clientes.models import Nombre_Cliente, Cliente
from ventas.models import Metodo_de_pago, Tasa, Impuesto
from reportes.models import Nota_de_entrega, Factura
# Register your models here.

admin.site.register(Compra)
admin.site.register(Producto)
admin.site.register(Nombre_Cliente)
admin.site.register(Cliente)
admin.site.register(Metodo_de_pago)
admin.site.register(Tasa)
admin.site.register(Impuesto)
admin.site.register(Nota_de_entrega)
admin.site.register(Factura)
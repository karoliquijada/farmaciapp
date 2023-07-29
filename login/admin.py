from django.contrib import admin
from compras.models import *
from proveedores.models import *
from productos.models import *
from clientes.models import *
from ventas.models import *
from reportes.models import *
# Register your models here.

#cliente
admin.site.register(Nombre_Cliente)
admin.site.register(Cliente)

#compras
#admin.site.register(Nombre_Supervisor)
admin.site.register(Compra)
#admin.site.register(MN_Compra_Producto)
#admin.site.register(MN_Compra_Proveedor)

#productos
admin.site.register(Categoria_Producto)
admin.site.register(Producto)
admin.site.register(MN_Subcategoria_Producto)

#proveedores
admin.site.register(Proveedor)

#reportes
admin.site.register(Nota_de_entrega)
admin.site.register(MN_NotaDeEntrega_MetodoDePago)
admin.site.register(MN_NotaDeEntrega_Producto)
admin.site.register(Factura)
admin.site.register(MN_Factura_Producto)
admin.site.register(MN_Factura_MetodoDePago)

#ventas
admin.site.register(Impuesto)
admin.site.register(Tasa)
admin.site.register(Metodo_de_pago)

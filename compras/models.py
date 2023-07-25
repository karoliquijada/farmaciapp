from productos.models import Producto
from proveedores.models import Proveedor
from django.db import models 

# Create your models here.

class Compra(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE, verbose_name='Producto')
    proveedor = models.ForeignKey(Proveedor, on_delete = models.CASCADE, verbose_name='Proveedor')
    fecha_de_compra = models.DateField(auto_now_add=True, verbose_name='Fecha')
    supervisor = models.CharField(max_length=500, verbose_name='Supervisor')
    inversion = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)

    def __str__(self):
        return self.id
    
    class Meta:

        db_table = 'Compra'
        verbose_name = 'Compras'
        verbose_name_plural = 'Compra'
        ordering = ['id']
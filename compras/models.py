from proveedores.models import Proveedor
from productos.models import Producto
from django.db import models 

# Create your models here.

class Supervisor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'Supervisor'
        verbose_name = 'Supervisor'
        verbose_name_plural = 'Supervisores'
        ordering = ['id']


class Compra(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    #supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    proveedor_id = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200, default="Descripcion")
    fecha_de_compra = models.DateField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Compra'
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        ordering = ['id']

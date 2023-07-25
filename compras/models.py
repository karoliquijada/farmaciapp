from productos.models import Producto
from proveedores.models import Proveedor
from django.db import models 

# Create your models here.

class Nombre_Supervisor(models.Model):
    cedula = models.CharField(max_length=500, primary_key=True, unique=True)
    primer_nombre = models.CharField(max_length=200)
    segundo_nombre = models.CharField(max_length=200, null=True, blank=True)
    primer_apellido = models.CharField(max_length=200)
    segundo_apellido = models.CharField(max_length=200, null=True, blank=True)
 
    def __str__(self):
        return (self.primer_nombre, self.primer_apellido)
    
    class Meta:
        db_table = 'Nombre_Supervisor'
        verbose_name = 'Nombre_Supervisor'
        verbose_name_plural = 'Nombres_Supervisores'
        ordering = ['cedula']

class Compra(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    fecha_de_compra = models.DateField(auto_now_add=True, verbose_name='Fecha')
    supervisor_cedula = models.ForeignKey(Nombre_Supervisor, on_delete = models.CASCADE, verbose_name='Supervisor_Cedula')
    inversion = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)

    def __str__(self):
        return self.id
    
    class Meta:
        db_table = 'Compra'
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        ordering = ['id']

class MN_Compra_Producto(models.Model):#COMPRA-PRODUCTO (M:N)
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    compra = models.ForeignKey(Compra, on_delete = models.CASCADE)
    id = models.AutoField(primary_key=True, unique=True)

    def __str__(self):
        return self.id
    
    class Meta:
        db_table = 'MN_Compra_Producto'
        verbose_name = 'MN_Compra_Producto'
        verbose_name_plural = 'MN_Compras_Productos'
        ordering = ['id']

class MN_Compra_Proveedor(models.Model):#COMPRA-PROVEEDOR (M:N)
    proveedor = models.ForeignKey(Proveedor, on_delete = models.CASCADE, verbose_name='Proveedor')
    compra = models.ForeignKey(Compra, on_delete = models.CASCADE)
    id = models.AutoField(primary_key=True, unique=True)

    def __str__(self):
        return self.id
    
    class Meta:
        db_table = 'MN_Compra_Proveedor'
        verbose_name = 'MN_Compra_Proveedor'
        verbose_name_plural = 'MN_Compra_Proveedor'
        ordering = ['id']
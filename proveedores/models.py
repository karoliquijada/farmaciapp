from django.db import models

# Create your models here.

class Proveedor(models.Model):
    rif = models.CharField(max_length=100, primary_key=True, unique=True, default=0)
    nombre = models.CharField(max_length=300, verbose_name='Proveedor')
    razon_social = models.CharField(max_length=500, verbose_name='Razon Social')
    direccion = models.CharField(max_length=500, verbose_name='Direccion')


    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Proveedor'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['rif']
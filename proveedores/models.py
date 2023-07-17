from django.db import models

# Create your models here.

class proveedor(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, default=0)
    proveedor = models.CharField(max_length=300, verbose_name='Proveedor')
    razon_social = models.CharField(max_length=500, verbose_name='Razon Social')
    direccion = models.CharField(max_length=500, verbose_name='Direccion')

    def __str__(self):
        return self.proveedor
    
    class Meta:
        db_table = 'Proveedor'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['id']
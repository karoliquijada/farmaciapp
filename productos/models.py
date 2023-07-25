from django.db import models

# Create your models here.

class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=5, unique=True, verbose_name='Codigo')
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    fecha_de_vencimiento = models.DateField(auto_now_add=True, verbose_name='Fecha')
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=0)
    imagen_de_producto = models.ImageField(upload_to='img_product', null=True, blank=True, verbose_name='Imagen')  

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['codigo']
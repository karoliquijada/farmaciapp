from django.db import models

# Create your models here.

class producto(models.Model):
    codigo = models.CharField(max_length=5, unique=True, verbose_name='Codigo')
    producto = models.CharField(max_length=150, verbose_name='Producto')
    fecha_de_vencimiento = models.DateField(auto_now_add=True, verbose_name='Fecha')
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=0)
    imagen_de_producto = models.ImageField(upload_to='img_product', null=True, blank=True, verbose_name='Imagen')  

    def __str__(self):
        return self.producto
    
    class Meta:
        db_table = 'Producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']
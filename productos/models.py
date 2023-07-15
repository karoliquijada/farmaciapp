from django.db import models

# Create your models here.

class producto(models.Model):
    codigo = models.CharField(max_length=5, anique=True, verbose_name='Codigo')
    producto = models.CharField(max_length=150, verbose_name='Producto')
    fecha_de_vencimiento = models.DateField(auto_now_add=True)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=0)



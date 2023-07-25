from django.db import models
from productos.models import Producto
from clientes.models import Cliente
from ventas.models import Metodo_de_pago

# Create your models here.

class Nota_de_entrega(models.Model):
    codigo = models.CharField(primary_key=True, max_length=5, unique=True, verbose_name='Codigo')
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    item = models.ForeignKey(Producto, on_delete=models.CASCADE)
    metodo_de_pago = models.ForeignKey(Metodo_de_pago, on_delete=models.CASCADE)
    total = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
        
    def __str__(self):
        return self.codigo
    
    class Meta:

        db_table = 'Nota_de_entrega'
        verbose_name = 'Nota_de_entrega'
        verbose_name_plural = 'Notas_de_entregas'
        ordering = ['codigo']

class Factura(models.Model):
    codigo = models.CharField(primary_key=True, max_length=5, unique=True, verbose_name='Codigo')
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    item = models.ForeignKey(Producto, on_delete=models.CASCADE)
    metodo_de_pago = models.ForeignKey(Metodo_de_pago, on_delete=models.CASCADE)
    subtotal = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
    igtf = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)

    def __str__(self):
        return self.codigo
    
    class Meta:

        db_table = 'Factura'
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'
        ordering = ['codigo']
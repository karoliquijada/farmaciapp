from django.db import models
from productos.models import Producto
from clientes.models import Cliente
from ventas.models import Metodo_de_pago

# Create your models here.

class Nota_de_entrega(models.Model):
    codigo = models.CharField(primary_key=True, max_length=5, unique=True, verbose_name='Codigo')
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    total = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
        
    def __str__(self):
        return self.codigo
    
    class Meta:
        db_table = 'Nota_de_entrega'
        verbose_name = 'Nota_de_entrega'
        verbose_name_plural = 'Notas_de_entregas'
        ordering = ['codigo']

class MN_NotaDeEntrega_MetodoDePago(models.Model):
    metodo_de_pago = models.ForeignKey(Metodo_de_pago, on_delete=models.CASCADE)
    nota_de_entrega = models.ForeignKey(Nota_de_entrega, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True, unique=True)

    def __str__(self):
        return self.id
    
    class Meta:
        db_table = 'MN_NotaDeEntrega_MetodoDePago'
        verbose_name = 'MN_NotaDeEntrega_MetodoDePago'
        verbose_name_plural = 'MN_NotasDeEntregas_MetodosDePagos'
        ordering = ['id']

class MN_NotaDeEntrega_Producto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nota_de_entrega = models.ForeignKey(Nota_de_entrega, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True, unique=True)

    def __str__(self):
        return self.id
    
    class Meta:
        db_table = 'MN_NotaDeEntrega_Producto'
        verbose_name = 'MN_NotaDeEntrega_Producto'
        verbose_name_plural = 'MN_NotasDeEntregas_Productos'
        ordering = ['id']

class Factura(models.Model):
    codigo = models.CharField(primary_key=True, max_length=5, unique=True, verbose_name='Codigo')
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
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

class MN_Factura_Producto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True, unique=True)

    def __str__(self):
        return self.id
    
    class Meta:
        db_table = 'MN_Factura_Producto'
        verbose_name = 'MN_Factura_Producto'
        verbose_name_plural = 'MN_Factura_Producto'
        ordering = ['id']

class MN_Factura_MetodoDePago(models.Model):
    metodo_de_pago = models.ForeignKey(Metodo_de_pago, on_delete=models.CASCADE)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True, unique=True)

    def __str__(self):
        return self.id
    
    class Meta:
        db_table = 'MN_Factura_MetodoDePago'
        verbose_name = 'MN_Factura_MetodoDePago'
        verbose_name_plural = 'MN_Facturas_MetodosDePagos'
        ordering = ['id']
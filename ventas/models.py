from django.db import models
from django.forms import model_to_dict
from clientes.models import Cliente
from productos.models import Producto



class Egreso(models.Model):
    fecha_pedido = models.DateField(max_length=255)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL , null=True , related_name='clientee')
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    pagado = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    comentarios = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    ticket = models.BooleanField(default=True)
    desglosar = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=True , null=True)

    class Meta:
        verbose_name='egreso'
        verbose_name_plural = 'egresos'
        order_with_respect_to = 'fecha_pedido'
    
    def __str__(self):
        return str(self.id)
   

class ProductosEgreso(models.Model):
    egreso = models.ForeignKey(Egreso, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=20, decimal_places=2 , null=False)
    precio = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    subtotal = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    iva = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    total = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    created = models.DateTimeField(auto_now_add=True)
    entregado = models.BooleanField(default=True)
    devolucion = models.BooleanField(default=False)

    class Meta:
        verbose_name='producto egreso'
        verbose_name_plural = 'productos egreso'
        order_with_respect_to = 'created'
    
    def __str__(self):
        return self.producto
    
    def toJSON(self):
        item = model_to_dict(self, exclude=['created'])
        return item


class Impuesto(models.Model):
    tipo = models.CharField(max_length=150, unique=True, primary_key=True)
    tasa = tasa = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)

    def __str__(self):
        return self.tipo
    
    class Meta:

        db_table = 'Impuesto'
        verbose_name = 'Impuesto'
        verbose_name_plural = 'Impuestos'
        ordering = ['tipo']


class Tasa(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    tasa = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
    
    class Meta:

        db_table = 'Tasas'
        verbose_name = 'Tasa'
        verbose_name_plural = 'Tasas'
        ordering = ['id']

class Metodo_de_pago(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=150)
    divisa = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)

    
    class Meta:

        db_table = 'Metodo_de_pago'
        verbose_name = 'Metodo_de_pago'
        verbose_name_plural = 'Metodos_de_pagos'
        ordering = ['id']



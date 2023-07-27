from django.db import models

# Create your models here.

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

    def __str__(self):
        return self.id
    
    class Meta:

        db_table = 'Tasas'
        verbose_name = 'Tasa'
        verbose_name_plural = 'Tasas'
        ordering = ['id']

class Metodo_de_pago(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=150)
    divisa = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)

    def __str__(self):
        return self.id
    
    class Meta:

        db_table = 'Metodo_de_pago'
        verbose_name = 'Metodo_de_pago'
        verbose_name_plural = 'Metodos_de_pagos'
        ordering = ['id']
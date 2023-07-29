from django.db import models

from django.db import models

# Create your models here.

class Cliente(models.Model):
    cedula = models.CharField(max_length=15, primary_key=True, unique=True)
    primer_nombre = models.CharField(max_length=200)
    segundo_nombre = models.CharField(max_length=200,blank=True, null=True)
    primer_apellido = models.CharField(max_length=200)
    segundo_apellido = models.CharField(max_length=200,blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    direccion = models.CharField(max_length=500)
    
    def __str__(self):
        return (self.cedula)
    
    class Meta:
        db_table = 'Cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['cedula']

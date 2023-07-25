from django.db import models

# Create your models here.

class Cliente(models.Model):
    cedula = models.CharField(max_length=15, primary_key=True, unique=True)
    telefono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=500)


    def __str__(self):
        return self.cedula
    
    class Meta:
        db_table = 'Cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['cedula']

class Nombre_Cliente(models.Model):
    cedula = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    primer_nombre = models.CharField(max_length=200)
    segundo_nombre = models.CharField(max_length=200)
    primer_apellido = models.CharField(max_length=200)
    segundo_apellido = models.CharField(max_length=200)
 
    def __str__(self):
        return (self.primer_nombre, self.primer_apellido)
    
    class Meta:
        db_table = 'Nombre_Cliente'
        verbose_name = 'Nombre_Cliente'
        verbose_name_plural = 'Nombres_Clientes'
        ordering = ['cedula']

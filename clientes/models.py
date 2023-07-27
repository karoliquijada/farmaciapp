from django.db import models

# Create your models here.

class Nombre_Cliente(models.Model):
    cedula = models.CharField(max_length=15, primary_key=True, unique=True)
    primer_nombre = models.CharField(max_length=200)
    segundo_nombre = models.CharField(max_length=200, null=True, blank=True)
    primer_apellido = models.CharField(max_length=200)
    segundo_apellido = models.CharField(max_length=200, null=True, blank=True)
 
    def __str__(self):
        return (self.primer_nombre, self.primer_apellido)
    
    class Meta:
        db_table = 'Nombre_Cliente'
        verbose_name = 'Nombre_Cliente'
        verbose_name_plural = 'Nombres_Clientes'
        ordering = ['cedula']


class Cliente(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    cedula = models.ForeignKey(Nombre_Cliente, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=500)


    def __str__(self):
        return self.cedula
    
    class Meta:
        db_table = 'Cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


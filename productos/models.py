from django.db import models

# Create your models here.

class Categoria_Producto(models.Model):
    categoria = models.CharField(max_length = 500, primary_key=True, unique=True)

    def __str__(self):
        return self.categoria
    
    class Meta:
        db_table = 'Categoria_Producto'
        verbose_name = 'Categoria_Producto'
        verbose_name_plural = 'Categorias_Productos'
        ordering = ['categoria']

class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=5, unique=True, verbose_name='Codigo')
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    fecha_de_vencimiento = models.DateField(auto_now_add=True, verbose_name='Fecha')
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=0)
    descuento = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    exento = models.BooleanField()
    imagen_de_producto = models.ImageField(upload_to='img_product', null=True, blank=True, verbose_name='Imagen')  

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['codigo']

class MN_Subcategoria_Producto(models.Model):#Categoria - Producto (MN)
    categoria = models.ForeignKey(Categoria_Producto, on_delete=models.CASCADE)
    codigo_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    subcategoria = models.CharField(max_length=500, primary_key=True, unique=True)

    def __str__(self):
        return self.subcategoria
    
    class Meta:
        db_table = 'Subcategoria_Producto'
        verbose_name = 'Subcategoria_Producto'
        verbose_name_plural = 'Subcategorias_Productos'
        ordering = ['subcategoria']

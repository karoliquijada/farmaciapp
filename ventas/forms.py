from django import forms
from clientes.models import Cliente
from productos.models import Producto

#Clientes Formularios #######################################
class AnadirClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('cedula','primer_nombre','primer_apellido','telefono','direccion')
        labels = {
            'cedula': 'Cédula de Identidad: ',
            'primer_nombre': 'Primer Nombre: ',
            'primer_apellido': 'Primer Apellido: ',
            'telefono': 'Nro. de Telefono: ',
            'direccion': 'Dirección del Cliente',
        }

class EditarClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('cedula','primer_nombre','primer_apellido','telefono','direccion')
        labels = {
            'cedula': 'Cédula de Identidad: ',
            'primer_nombre': 'Nombre: ',
            'primer_apellido': 'Apellido: ',
            'telefono': 'Nro. de Telefono: ',
            'direccion': 'Dirección del Cliente',
        }
        widgets = {
            'cedula': forms.TextInput(attrs={'type':'text','id': 'cedula_editar'}),
            'primer_nombre': forms.TextInput(attrs={'id': 'primer_nombre_editar'}),
            'primer_apellido': forms.TextInput(attrs={'id': 'primer_apellido_editar'}),
            'telefono': forms.TextInput(attrs={'id': 'tel_edt'}),
            'direccion': forms.TextInput(attrs={'id': 'dir_edt'}),

        }

#Productos Formularios #######################################
class AnadirProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo', 'nombre', 'precio', 'cantidad', 'descuento', 'exento')
        labels = {
            'codigo': 'Cod. Item: ',
            'nombre': 'Nombre del Item: ',
            'precio': 'Precio: ',
            'cantidad': 'Stock: ',
            'descuento': 'Descuento',
            'exento': 'Exento?',
        }

class EditarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo', 'nombre', 'precio', 'cantidad', 'descuento', 'exento')
        labels = {
            'codigo': 'Cod. Item: ',
            'nombre': 'Nombre del Item: ',
            'precio': 'Precio: ',
            'cantidad': 'Stock: ',
            'descuento': 'Descuento',
            'exento': 'Exento?',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'type':'text','id': 'codigo_editar'}),
            'nombre': forms.TextInput(attrs={'id': 'nombre_editar'}),
            'precio': forms.TextInput(attrs={'id': 'precio_editar'}),
            'cantidad': forms.TextInput(attrs={'id': 'cant_edt'}),
            'descuento': forms.TextInput(attrs={'id': 'desc_edt'}),
            'exento': forms.CheckboxInput(attrs={'id': 'exento_edt'}),

        }
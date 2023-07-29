from django import forms
from .models import Compra

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['proveedor_id', 'descripcion', 'fecha_de_compra', 'producto', 'total']
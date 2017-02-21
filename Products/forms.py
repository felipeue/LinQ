from django import forms
from Products.models import *


class RackForm(forms.ModelForm):

    class Meta:
        model = Rack
        fields = ('codigo', 'capacidad',)


class SkuForm(forms.ModelForm):

    class Meta:
        model = Sku
        fields = ('codigo', 'nombre_producto', 'fabricante', 'color',)


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('codigo', 'sku_producto',)


class RegistroForm(forms.ModelForm):

    class Meta:
        model = Registro
        exclude = ('fecha',)
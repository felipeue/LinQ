from __future__ import unicode_literals
from django.db import models
from datetime import datetime

# Create your models here.


class Rack(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    capacidad = models.IntegerField()

    def __unicode__(self):
        return unicode(self.codigo)


class Sku(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre_producto = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.nombre_producto)


class Producto(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    sku_producto = models.ForeignKey(Sku)

    def __unicode__(self):
        return unicode(self.codigo)


class Registro(models.Model):
    rack_contenedor = models.ForeignKey(Rack)
    fecha = models.DateTimeField(default=datetime.now)
    productos = models.ManyToManyField(Producto, blank=True)

    def __unicode__(self):
        return unicode(self.id)
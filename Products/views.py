from django.shortcuts import render
from Products.models import *
from Products.forms import *
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def agregar_sku(request):
    if request.method == 'POST':
        sku_form = SkuForm(data=request.POST)
        if sku_form.is_valid() :
            sku = sku_form.save()
            return HttpResponseRedirect('/')
        else:
            print sku_form.errors
    else:
        sku_form = SkuForm()

    return render(request, 'sku_form.html', {'sku_form': sku_form, })


def agregar_producto(request):
    if request.method == 'POST':
        producto_form = ProductoForm(data=request.POST)
        if producto_form.is_valid() :
            sku = producto_form.save()
            return HttpResponseRedirect('/')
        else:
            print producto_form.errors
    else:
        producto_form = ProductoForm()

    return render(request, 'producto_form.html', {'producto_form': producto_form, })


def agregar_rack(request):
    if request.method == 'POST':
        rack_form = RackForm(data=request.POST)
        if rack_form.is_valid() :
            sku = rack_form.save()
            return HttpResponseRedirect('/')
        else:
            print rack_form.errors
    else:
        rack_form = RackForm()

    return render(request, 'rack_form.html', {'rack_form': rack_form, })


def agregar_registro(request):
    if request.method == 'POST':
        registro_form = RegistroForm(data=request.POST)
        if registro_form.is_valid() :
            registro = registro_form.save()
            return HttpResponseRedirect('/')
        else:
            print registro_form.errors
    else:
        registro_form = RegistroForm()

    return render(request, 'registro_form.html', {'registro_form': registro_form, })
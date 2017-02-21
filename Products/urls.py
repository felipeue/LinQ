from django.conf.urls import url
from Products import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^agregar_sku/$', views.agregar_sku, name='as'),
    url(r'^agregar_registro/$', views.agregar_registro, name='ar'),
    url(r'^agregar_producto/$', views.agregar_producto, name='ap'),
    url(r'^agregar_rack/$', views.agregar_rack, name='ara'),
]
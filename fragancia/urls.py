from django.contrib import admin
from django.urls import path

from fragancia.views import (
    listar_Perfume, listar_Cliente, listar_Compra
)

urlpatterns = [
    path("perfumes/", listar_Perfume),
    path("clientes/", listar_Cliente),
    path("compras/", listar_Compra),
]

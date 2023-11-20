from django.contrib import admin
from django.urls import path

from fragancia.views import listar_Perfume, listar_Cliente, listar_Compra, buscar_perfume
from fragancia.views import PerfumeListView, PerfumeDetailView, PerfumeCreateView, PerfumeUpdateView, PerfumeDeleteView
from fragancia.views import ClienteListView, ClienteDetailView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView
from fragancia.views import CompraListView, CompraDetailView, CompraCreateView, CompraUpdateView, CompraDeleteView

urlpatterns = [
    path("perfumes/", listar_Perfume),
    path("clientes/", listar_Cliente),
    path("compras/", listar_Compra),
    path('perfumes/', PerfumeListView.as_view(), name='Perfume_list'),
    path('perfumes/<int:pk>/', PerfumeDetailView.as_view(), name='Perfume_detail'),
    path('perfumes/create/', PerfumeCreateView.as_view(), name='Perfume_create'),
    path('perfumes/buscar/', buscar_perfume.as_view(), name='Perfume_buscar'),
    path('perfumes/<int:pk>/update/', PerfumeUpdateView.as_view(), name='Perfume_update'),
    path('perfumes/<int:pk>/delete/', PerfumeDeleteView.as_view(), name='Perfume_delete'),
    path('perfumes/', ClienteListView.as_view(), name='Perfume_list'),
    path('perfumes/<int:pk>/', ClienteDetailView.as_view(), name='Perfume_detail'),
    path('perfumes/create/', ClienteCreateView.as_view(), name='Perfume_create'),
    path('perfumes/<int:pk>/update/', ClienteUpdateView.as_view(), name='Perfume_update'),
    path('perfumes/<int:pk>/delete/', ClienteDeleteView.as_view(), name='Perfume_delete'),
    path('perfumes/', CompraListView.as_view(), name='Perfume_list'),
    path('perfumes/<int:pk>/', CompraDetailView.as_view(), name='Perfume_detail'),
    path('perfumes/create/', CompraCreateView.as_view(), name='Perfume_create'),
    path('perfumes/<int:pk>/update/', CompraUpdateView.as_view(), name='Perfume_update'),
    path('perfumes/<int:pk>/delete/', CompraDeleteView.as_view(), name='Perfume_delete'),
]

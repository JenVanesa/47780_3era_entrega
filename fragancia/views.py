from django.shortcuts import render

from fragancia.models import Perfume, Cliente, Compra

# Create your views here.
def listar_Perfume(request):
    contexto = {
        'perfumes': Perfume.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='fragancia/perfumes.html',
        context=contexto,
    )
    return http_response

def listar_Cliente(request):
    contexto = {
        'clientes': Cliente.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='fragancia/perfumes.html',
        context=contexto,
    )
    return http_response

def listar_Compra(request):
    contexto = {
        'compras': Compra.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='fragancia/perfumes.html',
        context=contexto,
    )
    return http_response
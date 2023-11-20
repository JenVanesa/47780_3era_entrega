from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from fragancia.models import Perfume, Cliente, Compra
from fragancia.forms import PerfumeForm, ClienteForm, CompraForm

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

def crear_perfume(request):
    if request.method == "POST":
        # Guardado de datos
        # Creo un objeto formulario con la data que envio el usuario
        formulario = PerfumeForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            marca = data["marca"]
            aroma = data["aroma"]
            genero = data["genero"]
            precio = data["precio"]
            # creo un perfume en memoria RAM
            Perfume = Perfume(nombre=nombre, marca=marca, aroma=aroma, genero=genero, precio=precio)
            # Lo guardan en la Base de datos
            Perfume.save()

            # Redirecciono al usuario a la lista de perfumes
            url_exitosa = reverse('lista_perfumes') 
            return redirect(url_exitosa)
    else:  # GET
        # Descargar formulario inicial
        formulario = PerfumeForm()
    http_response = render(
        request=request,
        template_name='formulario_perfume.html',
        context={'formulario': formulario}
    )
    return http_response


def buscar_perfume(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        Perfume = Perfume.objects.filter(
            Q(nombre__icontains=busqueda) | Q(marca__contains=busqueda) | Q(aroma__contains=busqueda) | Q(genero__contains=busqueda)
        )

        contexto = {
            "Perfumes": Perfume,
        }
        http_response = render(
            request=request,
            template_name='lista_perfume.html',
            context=contexto,
        )
        return http_response



class PerfumeListView(ListView):
    model = Perfume
    template_name = 'fragancia/perfumes.html'
    context_object_name = 'perfumes'

class PerfumeDetailView(DetailView):
    model = Perfume
    template_name = 'fragancia/perfumes.html'
    context_object_name = 'perfume'

class PerfumeCreateView(CreateView):
    model = Perfume
    form_class = PerfumeForm
    template_name = 'fragancia/perfumes.html'
    success_url = '/fragancia/perfumes/'

class PerfumeUpdateView(UpdateView):
    model = Perfume
    form_class = PerfumeForm
    template_name = 'fragancia/perfumes.html'
    success_url = '/fragancia/perfumes/'

class PerfumeDeleteView(DeleteView):
    model = Perfume
    template_name = 'fragancia/perfumes.html'
    success_url = '/fragancia/perfumes/'

# Cliente views
class ClienteListView(ListView):
    model = Cliente
    template_name = 'fragancia/perfumes.html'
    context_object_name = 'clientes'

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'fragancia/perfumes.html'
    context_object_name = 'cliente'

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'fragancia/perfumes.html'
    success_url = '/fragancia/clientes/'

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'fragancia/perfumes.html'
    success_url = '/fragancia/clientes/'

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'fragancia/perfumes.html'
    success_url = '/fragancia/clientes/'

# Compra views
class CompraListView(ListView):
    model = Compra
    template_name = 'fragancia/perfumes.html'
    context_object_name = 'compras'

class CompraDetailView(DetailView):
    model = Compra
    template_name = 'fragancia/perfumes.html'
    context_object_name = 'compra'

class CompraCreateView(CreateView):
    model = Compra
    form_class = CompraForm
    template_name = 'fragancia/perfumes.html'
    success_url = '/fragancia/compras/'

class CompraUpdateView(UpdateView):
    model = Compra
    form_class = CompraForm
    template_name = 'fragancia/perfumes.html'
    success_url = '/fragancia/compras/'

class CompraDeleteView(DeleteView):
    model = Compra
    template_name = 'fragancia/perfumes.html'
    success_url = '/fragancia/compras/'
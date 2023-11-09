from django.shortcuts import render, redirect
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

class PerfumeListView(ListView):
    model = Perfume
    template_name = 'perfume_list.html'
    context_object_name = 'perfumes'

class PerfumeDetailView(DetailView):
    model = Perfume
    template_name = 'perfume_detail.html'
    context_object_name = 'perfume'

class PerfumeCreateView(CreateView):
    model = Perfume
    form_class = PerfumeForm
    template_name = 'perfume_form.html'
    success_url = '/perfumes/'

class PerfumeUpdateView(UpdateView):
    model = Perfume
    form_class = PerfumeForm
    template_name = 'perfume_form.html'
    success_url = '/perfumes/'

class PerfumeDeleteView(DeleteView):
    model = Perfume
    template_name = 'perfume_confirm_delete.html'
    success_url = '/perfumes/'

# Cliente views
class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente_list.html'
    context_object_name = 'clientes'

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente_detail.html'
    context_object_name = 'cliente'

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = '/clientes/'

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = '/clientes/'

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente_confirm_delete.html'
    success_url = '/clientes/'

# Compra views
class CompraListView(ListView):
    model = Compra
    template_name = 'compra_list.html'
    context_object_name = 'compras'

class CompraDetailView(DetailView):
    model = Compra
    template_name = 'compra_detail.html'
    context_object_name = 'compra'

class CompraCreateView(CreateView):
    model = Compra
    form_class = CompraForm
    template_name = 'compra_form.html'
    success_url = '/compras/'

class CompraUpdateView(UpdateView):
    model = Compra
    form_class = CompraForm
    template_name = 'compra_form.html'
    success_url = '/compras/'

class CompraDeleteView(DeleteView):
    model = Compra
    template_name = 'compra_confirm_delete.html'
    success_url = '/compras/'
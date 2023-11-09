from django import forms
from fragancia.models import Perfume, Cliente, Compra

class PerfumeForm(forms.ModelForm):
    class Meta:
        model = Perfume 
        fields = '__all__' 
        # fields = ['nombre', 'marca', 'precio'] # Para incluir solo algunos campos del model en el form
        # exclude = ['stock'] # Para excluir algunos campos del model del form

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'

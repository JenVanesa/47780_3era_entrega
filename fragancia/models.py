from django.db import models

# Create your models here.
class Perfume(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    aroma = models.CharField(max_length=50)
    genero = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('U', 'Unisex')])
    precio = models.DecimalField(max_digits=10, decimal_places=2)

def _str_(self):
        return f"{self.nombre} de {self.marca} con aroma a {self.aroma} para {self.genero}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

def _str_(self):
        return f"{self.nombre} {self.dni}"

class Compra(models.Model):
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

def _str_(self):
        return f"{self.cliente} compró {self.cantidad} unidades de {self.perfume} el {self.fecha} por {self.total}"

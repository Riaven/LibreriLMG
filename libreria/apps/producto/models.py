from django.db import models

class Tipo(models.Model):
    nombre = models.CharField(max_length = 30)

    def __str__ (self):
        return '{}'.format(self.nombre)

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length = 40)
    descripcion = models.CharField(max_length = 50)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    codigo = models.IntegerField()
    tipo = models.ForeignKey(Tipo, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)
from django.db import models
from inventory.models import TypeProduct


class Otros(models.Model):
    image = models.ImageField(upload_to="otros/", blank='', default="otros/subir.png")
    codigo = models.CharField(max_length=150, blank=True, unique=True)
    estado = models.BooleanField(default=True)
    nombre = models.CharField(max_length=150, blank=True)
    descripcion = models.CharField(max_length=300, blank=True)
    type_product = models.ForeignKey(TypeProduct, on_delete=models.CASCADE, related_name='otros')

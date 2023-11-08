from django.db import models
from inventory.models import TypeProduct


class Epp(models.Model):
    image = models.ImageField(upload_to="epp/", blank='', default="epp/subir.png")
    codigo = models.CharField(max_length=150, blank=True)
    estado = models.BooleanField(default=True)
    marca = models.CharField(max_length=150, blank=True)
    industria = models.CharField(max_length=150, blank=True)
    talla = models.CharField(max_length=150, blank=True)
    año_fabricacion = models.CharField(max_length=150, blank=True)
    color = models.CharField(max_length=150, blank=True)
    color_reflectivo = models.CharField(max_length=150, blank=True)
    certificacion = models.CharField(max_length=150, blank=True)
    color_suspensores = models.CharField(max_length=150, blank=True)
    material = models.CharField(max_length=150, blank=True)
    url = models.CharField(max_length=150, blank=True)
    type_product = models.ForeignKey(TypeProduct, on_delete=models.CASCADE, related_name='epp')

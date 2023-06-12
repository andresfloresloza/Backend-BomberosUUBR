from django.db import models
from inventory.models import TypeProduct


class HerramientasAccesorios(models.Model):
    image = models.ImageField(upload_to="herramientas_accesorios/", blank='',
                              default="herramientas_accesorios/subir.png")
    codigo = models.CharField(max_length=150, blank=True,unique=True)
    estado = models.BooleanField(default=True)
    marca = models.CharField(max_length=150, blank=True)
    industria = models.CharField(max_length=150, blank=True)
    color = models.CharField(max_length=150, blank=True)
    certificacion = models.CharField(max_length=150, blank=True)
    material = models.CharField(max_length=150, blank=True)
    type_product = models.ForeignKey(TypeProduct, on_delete=models.CASCADE, related_name='herramientas_accesorios')

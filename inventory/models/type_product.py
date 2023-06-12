from django.db import models


class TypeProduct(models.Model):
    name = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)


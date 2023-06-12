from django.contrib.auth.models import AbstractUser
from django.db import models


class BomberoUser(AbstractUser):
    username = models.CharField(max_length=50, blank=False, unique=True)
    password = models.CharField("password", max_length=128, null=True, blank=True)

    image = models.ImageField(upload_to="bombero/", blank='', default="bombero/perfil.png")
    legajo = models.CharField(max_length=100, blank=True,unique=True)
    state = models.BooleanField(default=True)
    grade = models.CharField(max_length=150, blank=True)
    address = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=150, blank=True)
    blood_type = models.CharField(max_length=150, blank=True,default="(A+)")

from django.contrib.auth.models import AbstractUser
from django.db import models


class BomberoUser(AbstractUser):
    username = models.CharField(max_length=50, blank=False, unique=True)
    password = models.CharField("password", max_length=128, null=True, blank=True, default="bomberosuubr0")

    image = models.ImageField(upload_to="bombero/", blank='', default="bombero/perfil.png")
    legajo = models.CharField(max_length=100, blank=True)
    cargo = models.CharField(max_length=150, blank=True)
    position = models.CharField(max_length=150, blank=True)
    state = models.CharField(max_length=150, blank=True)
    grade = models.CharField(max_length=150, blank=True)
    address = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=150, blank=True)
    blood_type = models.CharField(max_length=150, blank=True)

from django.urls import path, include
from rest_framework import routers

from authentication.api import BomberoViewSet

router = routers.DefaultRouter()
router.register(r'usuario', BomberoViewSet)

urlpatterns = [
    path('', include(router.urls))
]

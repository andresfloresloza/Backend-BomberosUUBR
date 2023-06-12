from django.urls import path, include
from rest_framework import routers

from inventory.api import EppEstructuralViewSet
from inventory.api.herramienta_accesorio_viewset import HerramientaAccesorioViewSet
from inventory.api.type_product_viewset import TypeProductViewSet

router = routers.DefaultRouter()
router.register(r'type-product', TypeProductViewSet)
router.register(r'epp-estructural-forestal', EppEstructuralViewSet)
router.register(r'herramientas-accesorios', HerramientaAccesorioViewSet)

urlpatterns = [
    path('', include(router.urls))
]

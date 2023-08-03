from django.urls import path, include
from rest_framework import routers

from inventory.api import EppViewSet
from inventory.api.otros_viewset import OtrosViewSet
from inventory.api.type_product_viewset import TypeProductViewSet

router = routers.DefaultRouter()
router.register(r'type-product', TypeProductViewSet)
router.register(r'epp', EppViewSet)
router.register(r'otros', OtrosViewSet)

urlpatterns = [
    path('', include(router.urls))
]

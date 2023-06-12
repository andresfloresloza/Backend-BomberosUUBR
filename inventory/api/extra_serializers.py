from rest_framework import serializers

from inventory.models import TypeProduct, EppEstructuralForestal


class TypeProductSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeProduct
        fields = ('id', 'name', 'category', 'epp_estructurals')


class EppEstructuralForestalSerializer(serializers.ModelSerializer):
    class Meta:
        model = EppEstructuralForestal
        fields = ('image', 'codigo', 'marca', 'industria', 'talla', 'año_fabricacion', 'color', 'color_reflectivo',
                  'certificacion', 'color_suspensores', 'material')


class HerramientaAccesorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EppEstructuralForestal
        fields = ('image', 'codigo', 'marca', 'industria', 'talla', 'año_fabricacion', 'color', 'color_reflectivo',
                  'certificacion', 'color_suspensores', 'material')

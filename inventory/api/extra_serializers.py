from rest_framework import serializers

from inventory.models import TypeProduct, Epp, Otros


class TypeProductSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeProduct
        fields = ('id', 'name', 'category')


class EppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Epp
        fields = ('image', 'codigo', 'marca', 'industria', 'talla', 'año_fabricacion', 'color', 'color_reflectivo',
                  'certificacion', 'color_suspensores', 'material')


class OtrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Otros
        fields = ('__all__')

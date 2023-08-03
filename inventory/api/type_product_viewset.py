from rest_framework import serializers, viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.validators import UniqueTogetherValidator

from inventory.models import TypeProduct


class TypeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeProduct
        fields = ('id', 'name', 'category')
        validators = [
            UniqueTogetherValidator(
                queryset=TypeProduct.objects.all(),
                fields=('name', 'category'),
                message='Este nombre ya existe en la categoría seleccionada.'
            )
        ]

class TypeProductViewSet(viewsets.ModelViewSet):
    serializer_class = TypeProductSerializer
    queryset = TypeProduct.objects.all()

    @permission_classes((IsAuthenticated, AllowAny))
    def create(self, request, *args, **kwargs):
        serializer = TypeProductSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"success": False, "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({"success": True, "data": serializer.data})

    @permission_classes((IsAuthenticated,))
    def retrieve(self, request, *args, **kwargs):
        obj_type_product = get_object_or_404(TypeProduct, pk=kwargs.get('pk'))
        type_product_serializer = TypeProductSerializer(obj_type_product)
        return Response(
            {"success": True,
             "data": {"type_product": type_product_serializer.data}})

    @permission_classes((IsAuthenticated,))
    def update(self, request, *args, **kwargs):
        obj_type_product = get_object_or_404(TypeProduct, pk=kwargs.get('pk'))
        type_product_serializer = TypeProductSerializer(obj_type_product, data=request.data, partial=True)
        if not type_product_serializer.is_valid():
            return Response({"success": False, "data": type_product_serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        type_product_serializer.save()
        return Response({"success": True, "data": type_product_serializer.data})

    @permission_classes((IsAuthenticated,))
    def destroy(self, request, *args, **kwargs):
        obj_type_product = get_object_or_404(TypeProduct, pk=kwargs.get('pk'))
        obj_type_product.delete()
        return Response({"success": True})

    @permission_classes((IsAuthenticated,))
    def list(self, request, *args, **kwargs):
        list_type_product = TypeProduct.objects.all()
        type_product_serializer = TypeProductSerializer(instance=list_type_product, many=True)
        return Response({"success": True, "list_type_product": type_product_serializer.data})

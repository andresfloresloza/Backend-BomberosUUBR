from rest_framework import serializers, viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes

from inventory.models import Otros


class OtrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Otros
        fields = ('__all__')


class OtrosViewSet(viewsets.ModelViewSet):
    serializer_class = OtrosSerializer
    queryset = Otros.objects.all()

    @permission_classes((IsAuthenticated, AllowAny))
    def create(self, request, *args, **kwargs):
        serializer = OtrosSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"success": False, "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({"success": True, "data": serializer.data})

    @permission_classes((IsAuthenticated,))
    def retrieve(self, request, *args, **kwargs):
        obj_otros = get_object_or_404(Otros, pk=kwargs.get('pk'))
        otros_serializer = OtrosSerializer(obj_otros)
        return Response(
            {"success": True,
             "data": {"otros": otros_serializer.data}})

    @permission_classes((IsAuthenticated,))
    def update(self, request, *args, **kwargs):
        obj_otros = get_object_or_404(Otros, pk=kwargs.get('pk'))
        otros_serializer = OtrosSerializer(obj_otros, data=request.data, partial=True)
        if not otros_serializer.is_valid():
            return Response({"success": False, "data": otros_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        otros_serializer.save()
        return Response({"success": True, "data": otros_serializer.data})

    @permission_classes((IsAuthenticated,))
    def destroy(self, request, *args, **kwargs):
        obj_otros = get_object_or_404(Otros, pk=kwargs.get('pk'))
        obj_otros.delete()
        return Response({"success": True})

    @permission_classes((IsAuthenticated,))
    def list(self, request, *args, **kwargs):
        list_otros = Otros.objects.all()
        otros_serializer = OtrosSerializer(instance=list_otros, many=True)
        return Response({"success": True, "list_otros": otros_serializer.data})

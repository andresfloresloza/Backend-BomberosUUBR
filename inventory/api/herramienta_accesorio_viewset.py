from rest_framework import serializers, viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes

from inventory.models import HerramientasAccesorios


class HerramientaAccesorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = HerramientasAccesorios
        fields = ('__all__')


class HerramientaAccesorioViewSet(viewsets.ModelViewSet):
    serializer_class = HerramientaAccesorioSerializer
    queryset = HerramientasAccesorios.objects.all()

    @permission_classes((IsAuthenticated, AllowAny))
    def create(self, request, *args, **kwargs):
        serializer = HerramientaAccesorioSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"success": False, "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({"success": True, "data": serializer.data})

    @permission_classes((IsAuthenticated,))
    def retrieve(self, request, *args, **kwargs):
        obj_herramienta_accesorio = get_object_or_404(HerramientasAccesorios, pk=kwargs.get('pk'))
        herramienta_accesorio_serializer = HerramientaAccesorioSerializer(obj_herramienta_accesorio)
        return Response(
            {"success": True,
             "data": {"herramienta_accesorio": herramienta_accesorio_serializer.data}})

    @permission_classes((IsAuthenticated,))
    def update(self, request, *args, **kwargs):
        obj_herramienta_accesorio = get_object_or_404(HerramientasAccesorios, pk=kwargs.get('pk'))
        herramienta_accesorio_serializer = HerramientaAccesorioSerializer(obj_herramienta_accesorio, data=request.data,
                                                                          partial=True)
        if not herramienta_accesorio_serializer.is_valid():
            return Response({"success": False, "data": herramienta_accesorio_serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        herramienta_accesorio_serializer.save()
        return Response({"success": True, "data": herramienta_accesorio_serializer.data})

    @permission_classes((IsAuthenticated,))
    def destroy(self, request, *args, **kwargs):
        obj_herramienta_accesorio = get_object_or_404(HerramientasAccesorios, pk=kwargs.get('pk'))
        obj_herramienta_accesorio.delete()
        return Response({"success": True})

    @permission_classes((IsAuthenticated,))
    def list(self, request, *args, **kwargs):
        list_herramienta_accesorio = HerramientasAccesorios.objects.all()
        herramienta_accesorio_serializer = HerramientaAccesorioSerializer(instance=list_herramienta_accesorio,
                                                                          many=True)
        return Response({"success": True, "list_herramienta_accesorio": herramienta_accesorio_serializer.data})

from rest_framework import serializers, viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes

from inventory.models import EppEstructuralForestal


class EppEstructuralSerializer(serializers.ModelSerializer):
    class Meta:
        model = EppEstructuralForestal
        fields = ('__all__')


class EppEstructuralViewSet(viewsets.ModelViewSet):
    serializer_class = EppEstructuralSerializer
    queryset = EppEstructuralForestal.objects.all()

    @permission_classes((IsAuthenticated, AllowAny))
    def create(self, request, *args, **kwargs):
        serializer = EppEstructuralSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"success": False, "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({"success": True, "data": serializer.data})

    @permission_classes((IsAuthenticated,))
    def retrieve(self, request, *args, **kwargs):
        obj_epp_estructural_forestal = get_object_or_404(EppEstructuralForestal, pk=kwargs.get('pk'))
        epp_estructural_forestal_serializer = EppEstructuralSerializer(obj_epp_estructural_forestal)
        return Response(
            {"success": True,
             "data": {"epp_estructural_forestal": epp_estructural_forestal_serializer.data}})

    @permission_classes((IsAuthenticated,))
    def update(self, request, *args, **kwargs):
        obj_epp_estructural_forestal = get_object_or_404(EppEstructuralForestal, pk=kwargs.get('pk'))
        epp_estructural_forestal_serializer = EppEstructuralSerializer(obj_epp_estructural_forestal, data=request.data,
                                                                       partial=True)
        if not epp_estructural_forestal_serializer.is_valid():
            return Response({"success": False, "data": epp_estructural_forestal_serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        epp_estructural_forestal_serializer.save()
        return Response({"success": True, "data": epp_estructural_forestal_serializer.data})

    @permission_classes((IsAuthenticated,))
    def destroy(self, request, *args, **kwargs):
        obj_epp_estructural_forestal = get_object_or_404(EppEstructuralForestal, pk=kwargs.get('pk'))
        obj_epp_estructural_forestal.delete()
        return Response({"success": True})

    @permission_classes((IsAuthenticated,))
    def list(self, request, *args, **kwargs):
        list_epp_estructural_forestal = EppEstructuralForestal.objects.all()
        epp_estructural_forestal_serializer = EppEstructuralSerializer(instance=list_epp_estructural_forestal,
                                                                       many=True)
        return Response({"success": True, "list_epp_estructural_forestal": epp_estructural_forestal_serializer.data})

from rest_framework import serializers, viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes

from inventory.models import Epp


class EppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Epp
        fields = ('__all__')


class EppViewSet(viewsets.ModelViewSet):
    serializer_class = EppSerializer
    queryset = Epp.objects.all()

    @permission_classes((IsAuthenticated, AllowAny))
    def create(self, request, *args, **kwargs):
        serializer = EppSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"success": False, "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({"success": True, "data": serializer.data})

    @permission_classes((IsAuthenticated,))
    def retrieve(self, request, *args, **kwargs):
        obj_epp = get_object_or_404(Epp, pk=kwargs.get('pk'))
        epp_serializer = EppSerializer(obj_epp)
        return Response(
            {"success": True,
             "data": {"epp": epp_serializer.data}})

    @permission_classes((IsAuthenticated,))
    def update(self, request, *args, **kwargs):
        obj_epp = get_object_or_404(Epp, pk=kwargs.get('pk'))
        epp_serializer = EppSerializer(obj_epp, data=request.data, partial=True)
        if not epp_serializer.is_valid():
            return Response({"success": False, "data": epp_serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        epp_serializer.save()
        return Response({"success": True, "data": epp_serializer.data})

    @permission_classes((IsAuthenticated,))
    def destroy(self, request, *args, **kwargs):
        obj_epp = get_object_or_404(Epp, pk=kwargs.get('pk'))
        obj_epp.delete()
        return Response({"success": True})

    @permission_classes((IsAuthenticated,))
    def list(self, request, *args, **kwargs):
        list_epp = Epp.objects.all()
        epp_serializer = EppSerializer(instance=list_epp, many=True)
        return Response({"success": True, "list_epp": epp_serializer.data})

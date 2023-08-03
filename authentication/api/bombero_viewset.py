from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password

from authentication.api import BomberoSimpleSerializer
from authentication.models import BomberoUser


class BomberoSerializer(serializers.ModelSerializer):
    username = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=BomberoUser.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    legajo = serializers.CharField(required=True, validators=[UniqueValidator(queryset=BomberoUser.objects.all())])

    class Meta:
        model = BomberoUser
        fields = (
            'id', 'username', 'password', 'password2', 'image', 'legajo', 'state', 'grade', 'first_name', 'last_name',
            'address', 'phone_number', 'blood_type', 'position')

    extra_kwargs = {
        'first_name': {'required': True},
        'last_name': {'required': True}
    }

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def validate_legajo(self, value):
        if self.instance is not None and self.instance.legajo == value:
            return value

        if BomberoUser.objects.filter(legajo=value).exists():
            raise serializers.ValidationError("El legajo ya está en uso.")

        return value

    def create(self, validated_data):
        user = BomberoUser.objects.create(
            username=validated_data.get('username'),
            legajo=validated_data.get('legajo'),
            state=validated_data.get('state'),
            grade=validated_data.get('grade'),
            position=validated_data.get('position'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            address=validated_data.get('address'),
            phone_number=validated_data.get('phone_number'),
            blood_type=validated_data.get('blood_type'),
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class BomberoViewSet(viewsets.ModelViewSet):
    queryset = BomberoUser.objects.all()
    serializer_class = BomberoSerializer

    @permission_classes((AllowAny,))
    def create(self, request, *args, **kwargs):
        user_serializer = BomberoSerializer(data=request.data)

        if not user_serializer.is_valid():
            return Response({"success": False, "data": user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        user_serializer.save()
        return Response({"success": True, "data": user_serializer.data})

    @permission_classes((IsAuthenticated,))
    def retrieve(self, request, *args, **kwargs):
        obj_user = get_object_or_404(BomberoUser, pk=kwargs.get('pk'))
        user_serializer = BomberoSerializer(obj_user)
        return Response(
            {"success": True,
             "data": {"user": user_serializer.data}})

    @permission_classes((IsAuthenticated,))
    def update(self, request, *args, **kwargs):
        obj_user = get_object_or_404(BomberoUser, pk=kwargs.get('pk'))
        user_serializer = BomberoSerializer(instance=obj_user, data=request.data, partial=True)

        if not user_serializer.is_valid():
            return Response({"success": False, "data": user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        if 'password' in request.data:
            password = make_password(request.data['password'])
            user_serializer.validated_data['password'] = password

        user_serializer.save()
        return Response({"success Update": True, "data": user_serializer.data})

    @permission_classes((IsAuthenticated,))
    def destroy(self, request, *args, **kwargs):
        obj_user = get_object_or_404(BomberoUser, pk=kwargs.get('pk'))
        obj_user.delete()
        return Response({'success': True})

    @permission_classes((IsAuthenticated,))
    def list(self, request, *args, **kwargs):
        lista_usuarios = BomberoUser.objects.all()
        user_serializer = BomberoSimpleSerializer(lista_usuarios, many=True)
        return Response({"success": True, "list_users": user_serializer.data})

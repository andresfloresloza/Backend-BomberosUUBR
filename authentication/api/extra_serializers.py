from rest_framework import serializers

from authentication.models import BomberoUser


class BomberoSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BomberoUser
        fields = (
            '__all__')

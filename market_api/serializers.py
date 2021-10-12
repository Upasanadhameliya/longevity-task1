from base.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
from account.models import User


class LongevitySerializer(ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=User.objects.all()
    )

    class Meta:
        model = LongevityParams
        fields = "__all__"


class WelltorySerializer(ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=User.objects.all()
    )

    class Meta:
        model = WelltoryParams
        fields = "__all__"

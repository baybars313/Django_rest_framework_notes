from rest_framework import serializers
from .models import Drv
class Create_drv(serializers.Serializer):
    name=serializers.CharField(max_length=255)
    age=serializers.CharField(max_length=255)
    phone=serializers.CharField(max_length=255)

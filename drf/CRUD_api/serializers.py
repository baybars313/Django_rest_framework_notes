from rest_framework import serializers
from serializer.models import Drv



class Update_drv(serializers.Serializer):
    name=serializers.CharField(max_length=255)
    age=serializers.CharField(max_length=255)
    phone=serializers.CharField(max_length=255)

    def update(self, instance, validate_data):
        instance.name=validate_data.get("name", instance.name)
        instance.age=validate_data.get("age", instance.age)
        instance.phone=validate_data.get("phone", instance.phone)
        instance.save()
        return instance

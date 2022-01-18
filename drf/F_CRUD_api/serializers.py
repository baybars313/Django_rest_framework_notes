from rest_framework import serializers
from serializer.models import *


class model_serializer(serializers.ModelSerializer):
	class Meta:
		model=Drv
		fields='__all__'
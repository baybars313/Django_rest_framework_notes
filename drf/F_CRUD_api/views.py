from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializer.models import *
from .serializers import model_serializer


@api_view(['GET','POST','DELETE','PUT'])
def driver_view(request):
	if request.method=='POST':
		data=request.data
		serializer=model_serializer(data=data)
		if serializer.is_valid():
			serializer.save()
		return Response("{'type':'post'}")
	elif request.method=='PUT':
		data=request.data
		id=request.data.get('id')
		drv=Drv.objects.get(id=id)
		serializer=model_serializer(drv, data=data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response("{'type':'put' }")
		else:
			return Response(serializer.error)
	elif request.method=='DELETE':
		id=request.data.get('id')
		drv=Drv.objects.get(id=id)
		drv.delete()
		return Response("{'type':'DELETE' }")
	elif request.method=='GET':
		id=request.data.get('id')
		if id is not None:
			drv=Drv.objects.get(id=id)
			serializer=model_serializer(drv)
			return Response(serializer.data)
		else:
			return Response("{'type':'no id specified' }")



def end_pnt(request,pk=None):
	if request.method=='GET':
		id=pk
		if id is not None:
			drv=Drv.objects.get(id=pk)
			serializer=model_serializer(drv)
			return Response(serializer.data)
		else:
			return Response("{'type':'no id specified' }")

    

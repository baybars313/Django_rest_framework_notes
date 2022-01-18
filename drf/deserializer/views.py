from django.shortcuts import render
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import Create_drv
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
@csrf_exempt
def Create_driver(request):
    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        dessrializer=Create_drv(data=python_data)
        if dessrializer.is_valid():
            dessrializer.save()
            res={
            "status":"ok"
            }
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="aplication/json")
        json_data=JSONRenderer().render(deserializer.error)
        return HttpResponse(json_data, content_type="aplication/json")

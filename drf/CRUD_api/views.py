from django.shortcuts import render
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import Update_drv
from serializer.models import Drv
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
@csrf_exempt
def updateDrv(request):
    if request.method== "PUT":
        data=request.body
        stream=io.BytesIO(data)
        python_data=JSONParser().parse(stream)
        id=python_data.get("id")
        drv=Drv.objects.get(id=id)
        update=Update_drv(drv, data=python_data, partial=True)
        if update.is_valid():
            update.save()
            res={
            "status":"ok"
            }
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="aplication/json")
        json_data=JSONRenderer().render(update.error)
        return HttpResponse(json_data, content_type="aplication/json")

    if request.method== "DELETE":
        data=request.body
        stream=io.BytesIO(data)
        python_data=JSONParser().parse(stream)
        id=python_data.get("id")
        drv=Drv.objects.get(id=id)
        drv.delete()
        res={
        "status":"deleted"
        }
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data, content_type="aplication/json")

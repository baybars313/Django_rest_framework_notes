from django.shortcuts import render
from .models import *
from .serializers import Create_drv
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
#serializers
def drv_info(request,pk):
    drv=Drv.objects.filter(name=pk)
    serialized=Create_drv(drv, many=True)
    return JsonResponse(serialized.data, safe=False)
    # both ways area correct
    # json_dat=JSONRenderer().render(serialized.data)
    #
    # return HttpResponse(json_dat, content_type="application/json")

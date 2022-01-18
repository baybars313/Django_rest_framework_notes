from django.urls import path
from .views import *

urlpatterns = [
     path("postapi/", Create_driver , name="drv_info" ),
]

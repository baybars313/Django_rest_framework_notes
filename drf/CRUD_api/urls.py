from django.urls import path
from .views import *

urlpatterns = [
    path("updateapi/", updateDrv, name="update"),
    
]

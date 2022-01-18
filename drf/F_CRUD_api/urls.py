from django.urls import path
from .views import *

urlpatterns = [
    path("func_get/", driver_view, name="func_driver"),
    path("func_get1/<int:pk>/", end_pnt, name="func_drivers"),
    
]

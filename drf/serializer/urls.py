from django.urls import path
from .views import drv_info

urlpatterns = [
    path("getapi/<str:pk>/", drv_info , name="drv_info" ),
]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("main.urls")),
    path("serializer/",include("serializer.urls")),
    path("deserializer/",include("deserializer.urls")),
    path("func_crud/",include("F_CRUD_api.urls")),
    path("crud/",include("CRUD_api.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

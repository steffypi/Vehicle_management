from django.contrib import admin
from django.urls import path, include
from vehicle import views


urlpatterns = [
    path('admin/', admin.site.urls),
]
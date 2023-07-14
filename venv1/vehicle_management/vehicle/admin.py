from django.contrib import admin
from vehicle.models import CustomUser,Vehicles

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Vehicles)
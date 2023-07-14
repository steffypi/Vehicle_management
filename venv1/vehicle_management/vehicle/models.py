from django.db import models
from django.contrib.auth.models import AbstractUser,User
# Create your models here.

class Vehicles(models.Model):
    VEHICLE_TYPES = [
        ('Two', 'Two Wheeler'),
        ('Three', 'Three Wheeler'),
        ('Four', 'Four Wheeler')
    ]
    vehicle_number = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(max_length=10,choices=VEHICLE_TYPES)
    vehicle_model = models.CharField(max_length=100)
    vehicle_description = models.TextField(max_length=100)

    def __str__(self):
        return self.vehicle_number

class CustomUser(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)


from django import forms
from vehicle.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from vehicle.models import CustomUser,Vehicles

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields
        
class vehicleform(forms.ModelForm):
    class Meta:
        model=Vehicles
        fields='__all__'
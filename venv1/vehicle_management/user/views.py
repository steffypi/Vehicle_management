from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from user.forms import CustomUserCreationForm,vehicleform
from django.views.generic import ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from vehicle.models import Vehicles

def view(requset):
    return render(requset, "users.html")

def user_signup(request):
    form=CustomUserCreationForm()
    if(request.method=="POST"):
        form=CustomUserCreationForm(request.POST)
        if(form.is_valid()):
            f=form.save(commit=False)
            f.is_superadmin=True
            f.save()
            return view(request)
    return render(request,'user_signup.html',{'form':form})

class vehicleListView(ListView):
    model=Vehicles
    template_name="userview.html"
    context_object_name="vehicles"
    
class adminvehicleListView(ListView):
    model=Vehicles
    template_name="adminview.html"
    context_object_name="vehicle"
    
class adminvehicleupdateview(UpdateView):
    model=Vehicles
    template_name="adminedit.html"
    fields=['vehicle_type','vehicle_model','vehicle_description']
    success_url = reverse_lazy('user:adminvehicleListView')


class supervehicleListView(ListView):
    model = Vehicles
    template_name = "superview.html"
    context_object_name = "vehicle"


class supervehicleupdateview(UpdateView):
    model = Vehicles
    template_name = "superedit.html"
    fields = ['vehicle_type', 'vehicle_model', 'vehicle_description']
    success_url = reverse_lazy('user:supervehicleListView')

class superdeletevehicleview(DeleteView):
    model=Vehicles
    template_name="superdelete.html"
    success_url = reverse_lazy('user:supervehicleListView')
    

class supercreatevehicle(CreateView):
    model=Vehicles
    template_name="supercreate.html"
    fields=['vehicle_type', 'vehicle_model', 'vehicle_description']
    success_url=reverse_lazy('user:supervehicleListView')

def users_login(request):
    if request.method == 'POST':
        username = request.POST.get('u')
        password = request.POST.get('p')
        user= authenticate(username=username, password=password)
        if user and user.is_user == True:
            login(request,user)
            list_view = vehicleListView()
            queryset = list_view.get_queryset()
            rendered_output = render(request, list_view.template_name, {list_view.context_object_name: queryset})
            html_content = rendered_output.content.decode('utf-8')
            return render(request, 'context_object.html', {'rendered_output': html_content,'context_object_name': list_view.context_object_name})
        elif user and user.is_admin == True:
            login(request, user)
            list_view = adminvehicleListView()
            queryset = list_view.get_queryset()
            rendered_output = render(request, list_view.template_name, {list_view.context_object_name: queryset})
            html_content = rendered_output.content.decode('utf-8')
            return render(request, 'context_object1.html', {'rendered_output': html_content,'context_object_name': list_view.context_object_name})
        elif user and user.is_superadmin == True:
            login(request, user)
            list_view = supervehicleListView()
            queryset = list_view.get_queryset()
            rendered_output = render(request, list_view.template_name, {list_view.context_object_name: queryset})
            html_content = rendered_output.content.decode('utf-8')
            return render(request, 'context_object2.html', {'rendered_output': html_content,'context_object_name': list_view.context_object_name})
            
        else:
            return HttpResponse("Invalid login details.....")
    return render(request, 'users_login.html')


def user_logout(request):
    logout(request)
    return view(request)


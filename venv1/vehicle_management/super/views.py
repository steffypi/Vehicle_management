from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from user.forms import CustomUserCreationForm
from user.views import view

def signup(request):
    form=CustomUserCreationForm()
    if(request.method=="POST"):
        form=CustomUserCreationForm(request.POST)
        if(form.is_valid()):
            f=form.save(commit=False)
            f.is_superadmin=True
            f.save()
            return view(request)
    return render(request,'super_signup.html',{'form':form})

def super_logout(request):
    logout(request)
    return view(request)


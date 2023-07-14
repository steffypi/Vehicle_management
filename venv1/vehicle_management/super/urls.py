from django.contrib import admin
from django.urls import path, include
from super import views

app_name="super"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', views.super_logout, name="super_logout"),
    path('super_signup/', views.signup,name="signup"),
] 
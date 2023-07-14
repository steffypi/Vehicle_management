from django.contrib import admin
from django.urls import path, include
from adminuser import views

app_name="adminuser"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', views.admin_logout, name="admin_logout"),
    path('admin_signup/', views.admin_signup,name="admin_signup"),
]
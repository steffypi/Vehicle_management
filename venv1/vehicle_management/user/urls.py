from django.contrib import admin
from django.urls import path, include
from user import views

app_name="user"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.view,name="view_vehicle"),
    path('users_login/',views.users_login,name="users_login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('user_signup/', views.user_signup, name="user_signup"),
    path('view_vehicle/',views.vehicleListView.as_view(),name="vehicleListView"),
    path('admin_view_vehicle/', views.adminvehicleListView.as_view(), name="adminvehicleListView"),
    path('edit/<str:pk>/',views.adminvehicleupdateview.as_view(),name="adminvehicleupdateview"),
    path('super_view_vehicle/', views.supervehicleListView.as_view(), name="supervehicleListView"),
    path('superedit/<str:pk>/', views.supervehicleupdateview.as_view(), name="supervehicleupdateview"),
    path('delete//<int:pk>/',views.superdeletevehicleview.as_view(),name="superdeletevehicleview"),
    path('addvehicle/', views.supercreatevehicle.as_view(), name="supercreatevehicle"),

]
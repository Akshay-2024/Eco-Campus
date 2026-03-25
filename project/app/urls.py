from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [

    
    path('', views.home, name='home'),
    path('signup/', views.sign, name='signin'),
    path('login/', views.log, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile,name="profile"),
    path('leader/', views.leader,name="leader"),
    path('admins/', views.admin,name="admin"),
    path('events/', views.event,name="event"),
]
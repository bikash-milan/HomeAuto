
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.Login,name='login'),
    path('logout',views.logout,name='logout'),
    path('dash',views.dashboard,name='dashboard'),
    path('update',views.updateprofile,name='update')
]

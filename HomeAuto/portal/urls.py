from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name='index'),
    path('login',views.Login,name='login'),
    path('logout',views.Logout,name='logout')
]

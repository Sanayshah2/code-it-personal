from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.Login,name='login'),

    path('logout/', views.logout_view, name='logout_view'),
    path('add-requirement/', views.addRequirement, name='addRequirement'),
    path('ngo-dashboard/', views.ngoDashboard, name='ngoDashboard'),




]
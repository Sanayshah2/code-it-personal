from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.Login,name='login'),
    path('<username>/donordashboard/',views.donordashboard,name='donordashboard'),
    path('<username>/ngodashboard/',views.ngodashboard,name='ngodashboard'),
    path('logout/', views.logout_view, name='logout_view'),




]
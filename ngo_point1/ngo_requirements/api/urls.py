from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('requirementlist/<username>/', views.NgoRequirementList.as_view(), name = 'ngo-specific-requirement-list'),
    path('requirementlist/', views.RequirementList.as_view(), name = 'requirement-list'),
    path('categorylist/', views.CategoryList.as_view(), name = 'category-list'),



]
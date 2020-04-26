from django.urls import path
from . import views

urlpatterns = [
    path('plant', views.plant_list, name='plant_list'),
    path('plant/<int:pk>/', views.plant_detail, name='plant_detail'),
]
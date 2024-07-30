
from django.contrib import admin
from django.urls import path
from .views import home_view, imageDetail_view
urlpatterns = [
    path('',home_view, name='home'),
    path('<int:pk>/',imageDetail_view, name='image_detail'),
]

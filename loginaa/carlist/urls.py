from django.urls import path, include
from .views import Carlist, CarRegistration
from . import views

urlpatterns = [
    path('', views.Carlist, name='carlist'),
    path('registration', views.CarRegistration, name='registration'),
]
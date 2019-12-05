from django.urls import path, include
from .views import Carlist
from . import views

urlpatterns = [
    path('', views.Carlist, name='carlist'),
    path('registration', views.CarRegistration, name='registration'),
    path('myregcars',views.Myregisteredcar, name='myregcars'),
    path('myregcars/(?<pk>\d+)', views.Cardetail, name='cardetail'),
]
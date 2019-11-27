from django.forms import forms, ModelForm
from .views import *
from .models import *
from django import forms


class CarFsell(ModelForm):

    class Meta:
        model = Car
        fields = ['id', 'car_model', 'fuel_type', 'transmission_type', 'price', 'mil', 'current_city']


class CarFimage(ModelForm):

    class Meta:
        model= CarImages
        fields = ['image']


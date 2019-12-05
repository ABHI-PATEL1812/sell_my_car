from django.forms import forms, ModelForm
from .views import *
from .models import *



class CarFsell(ModelForm):

    class Meta:
        model = Car
        fields = ['car_model', 'fuel_type', 'transmission_type', 'price', 'mil', 'current_city', 'image', 'image1','image2']



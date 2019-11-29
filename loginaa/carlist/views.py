from django.shortcuts import render
from .models import *

# Create your views here.
from django.views.generic import CreateView

from .forms import CarFsell, CarFimage


def CarRegistration(request):

    form_reg = CarFsell
    return render(request, 'registermycar.html', {'freg': form_reg})


def Carlist(request):

    if request.method == 'POST':
        form = CarFsell(request.POST, request.FILES)
        if form.is_valid():

            u = form.save()
            cars = Car.objects.all()
            return render(request, 'carlist.html', {'cars': cars})
        else:
            form_reg = CarFsell
            return render(request, 'registermycar.html', {'freg': form_reg})
    else:
        cars = Car.objects.all()
        return render(request, 'carlist.html', {'cars': cars})
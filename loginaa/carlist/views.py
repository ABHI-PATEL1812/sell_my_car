from django.db.models import Q
from django.shortcuts import render
from .models import *

# Create your views here.
from django.views.generic import CreateView

from .forms import CarFsell


def CarRegistration(request):

    form_reg = CarFsell
    return render(request, 'registermycar.html', {'freg': form_reg})


def Carlist(request):

    if request.method == 'POST':
        form = CarFsell(request.POST, request.FILES)
        if form.is_valid():
            u = form.save(commit=False)
            ab = request.user
            u.added_by= ab
            u.user_id = ab.id
            u.save()
            cars = Car.objects.filter(user_id=ab.id)
            return render(request, 'myregcars.html', {'cars': cars})
        else:
            form_reg = CarFsell
            return render(request, 'registermycar.html', {'freg': form_reg})
    else:
        ab = request.user
        cars = Car.objects.filter(~Q(user_id=ab.id))
        return render(request, 'carlist.html', {'cars': cars})


def Myregisteredcar(request):

    cars = Car.objects.filter(user_id=request.user.id)
    return render(request, 'myregcars.html', {'cars':cars})


def Cardetail(request, pk):
    cars =Car.objects.filter(id=pk)
    return render(request, 'cardetail.html', {'cars':cars})

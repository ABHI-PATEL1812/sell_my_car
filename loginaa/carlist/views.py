from django.shortcuts import render
from .models import *

# Create your views here.
from django.views.generic import CreateView

from .forms import CarFsell, CarFimage


def CarRegistration(request):

    form_reg = CarFsell
    form_image = CarFimage
    return render(request, 'registermycar.html', {'freg': form_reg, 'fimg': form_image})


def Carlist(request):

    if request.method == 'POST':
        form = CarFsell(request.POST)
        form2 = CarFimage(request.POST, request.FILES)
        if form.is_valid():
            u = form.save()
        if form2.is_valid():
            u2 = form2.save()

    users = Car.objects.all()
    image = CarImages.objects.all()
    return render(request, 'carlist.html', {'users': users, 'image': image})
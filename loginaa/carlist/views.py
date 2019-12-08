from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
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
            return redirect(Myregisteredcar)
        else:
            form_reg = CarFsell
            return render(request, 'registermycar.html', {'freg': form_reg})
    else:
        ab = request.user
        cars = Car.objects.filter(~Q(user_id=ab.id))
        return render(request,'carlist.html', {'cars': cars})


def Myregisteredcar(request):

    cars = Car.objects.filter(user_id=request.user.id)
    return render(request, 'myregcars.html', {'cars':cars})


def Cardetail(request, pk):
    cars =Car.objects.filter(id=pk)
    return render(request, 'cardetail.html', {'cars':cars})


def Likeoncar(request):

    if request.method == 'GET':
        likedcar_id = request.GET['car_id']
        likinguser = request.user.id
        try:
            likedcar_obj = Likes.objects.get(liked_car_id=likedcar_id, liking_user=likinguser)
            likedcar_obj.delete()
        except Likes.DoesNotExist:
            like = Likes.objects.create(liked_car_id=likedcar_id, liking_user=likinguser)

def Updatecar(request, pk):
    car_obj = Car.objects.get(id=pk)
    car_form =  CarFsell(request.POST or None, instance=car_obj)
    if request.method == 'POST':
        if car_form.is_valid():
            u = car_form.save(commit=False)
            u.added_by = request.user
            u.user_id = request.user.id
            u.save()
            cars = Car.objects.filter(id=pk)
            return redirect(Cardetail, pk)
        else:
            return render(request, 'registermycar.html', {'freg': car_form})
    else:
        return render(request, 'registermycar.html', {'freg': car_form})


def Deletecar(request, pk):
    try:
        car_obj = Car.objects.get(id=pk)
    except Car.DoesNotExist:
        return HttpResponse('car not exist')
    car_obj.delete()
    return redirect(Myregisteredcar)


from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class HomePageView(TemplateView):
    template_name = 'home.html'

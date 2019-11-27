from django.urls import path, include
from .views import SignUp, HomePageView


urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('', HomePageView.as_view(), name='home'),
    path('carlist', include('carlist.urls')),
]
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(CarCompany)
admin.site.register(Car)
admin.site.register(CurrentCity)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(Likes)

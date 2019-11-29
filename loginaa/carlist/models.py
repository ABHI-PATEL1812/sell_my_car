from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# Create your models here.
# change the imagefield value to be the newley modifed image value
#      self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.cars.id, 'image/jpeg',
#                                     sys.getsizeof(output), None)

class CarCompany(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class CarModel(models.Model):

    c_model = models.CharField(max_length=30, help_text='enter car model name')
    c_name = models.ForeignKey('CarCompany', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.c_model

    class Meta:
        ordering = ['c_model']


class CarModelAdmin(admin.ModelAdmin):
    list_display = ('c_model', 'c_name')


class OwnerDetail(models.Model):

    f_name = models.CharField(max_length=20, help_text='owner name')
    mobile = PhoneNumberField(max_length=13, unique=True)
    city = models.ForeignKey('CurrentCity', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.f_name}'


class CurrentCity(models.Model):
    name = models.CharField(max_length=20, help_text='Enter city name')

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.UUIDField(auto_created=True, default=uuid.uuid4(), primary_key=True)
    car_model = models.ForeignKey('CarModel', on_delete=models.SET_NULL, null=True)
    FUEL_TYPE = (
        ('p', 'Petrol'),
        ('d', 'Deisel'),
    )
    fuel_type = models.CharField(
        max_length=6,
        choices=FUEL_TYPE,
        default='p',
    )
    TRANSMISSION = (
        ('m', 'manual'),
        ('a', 'automatic'),
    )
    transmission_type = models.CharField(
        max_length=1,
        choices=TRANSMISSION,
        default='m'
    )
    price = models.IntegerField(default=0)
    mil = models.FloatField(default=0)
    current_city = models.ForeignKey('CurrentCity', on_delete=models.SET_NULL, null=True)
    owner_detail = models.ForeignKey('OwnerDetail', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.car_model}'


class CarImages(models.Model):
    carid = models.CharField(max_length=40)
    image = models.ImageField()

    def save(self):
        # Opening the uploaded image
        im = Image.open(self.image)

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((300, 300))

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.carid, 'image/jpeg',
                                        sys.getsizeof(output), None)

        super(CarImages, self).save()

    def __str__(self):
        return f'{self.carid}'

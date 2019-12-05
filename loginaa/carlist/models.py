from django.contrib.auth.models import User

from loginaa import settings
from users.models import CustomUser
from django.contrib import admin
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# Create your models here.


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


class CurrentCity(models.Model):
    name = models.CharField(max_length=20, help_text='Enter city name')

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
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
    KM_DRIVEN = (
        ('a', '0-5000'),
        ('b', '5000-10000'),
        ('c', '10000-15000'),
        ('d', '15000-25000'),
        ('e', '25000-35000'),
        ('f', '35000-50000'),
        ('g', '50000-70000'),
        ('h', '70000-100000'),
    )
    km_driven = models.CharField(
        max_length=1,
        choices=KM_DRIVEN,

    )
    REGISTRATION_YEAR = (
        ('a','2010'),
        ('b', '2011'),
        ('c', '2012'),
        ('d', '2013'),
        ('e', '2014'),
        ('f', '2015'),
        ('g', '2016'),
        ('h', '2017'),
        ('h', '2018'),
        ('h', '2019'),
    )
    reg_year = models.CharField(
        max_length=1,
        choices=REGISTRATION_YEAR,

    )
    price = models.IntegerField(default=0)
    mil = models.FloatField(default=0)
    current_city = models.ForeignKey('CurrentCity', on_delete=models.SET_NULL, null=True)
    image = models.ImageField()
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    user_id = models.IntegerField()


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
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.id, 'image/jpeg',
                                          sys.getsizeof(output), None)
        print(self.id)

        #secind image
        if self.image1:
            im1 = Image.open(self.image1)
            output = BytesIO()
            im1 = im1.resize((300, 300))
            im1.save(output, format='JPEG', quality=100)
            output.seek(0)
            self.image1 = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.id, 'image/jpeg',
                                          sys.getsizeof(output), None)

          #third image
        if self.image2:
            im2 = Image.open(self.image2)
            output = BytesIO()
            im2 = im2.resize((300, 300))
            im2.save(output, format='JPEG', quality=100)
            output.seek(0)
            self.image2 = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.id, 'image/jpeg',
                                          sys.getsizeof(output), None)

        super(Car, self).save()

    def __str__(self):
        return f'{self.car_model},{self.id}'



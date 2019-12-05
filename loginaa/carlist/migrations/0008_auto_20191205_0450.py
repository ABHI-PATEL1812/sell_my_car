# Generated by Django 2.2.7 on 2019-12-05 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carlist', '0007_auto_20191203_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='km_driven',
            field=models.CharField(choices=[('a', '0-5000'), ('b', '5000-10000'), ('c', '10000-15000'), ('d', '15000-25000'), ('e', '25000-35000'), ('f', '35000-50000'), ('g', '50000-70000'), ('h', '70000-100000')], default='c', max_length=1),
        ),
        migrations.AddField(
            model_name='car',
            name='reg_year',
            field=models.CharField(choices=[('a', '2010'), ('b', '2011'), ('c', '2012'), ('d', '2013'), ('e', '2014'), ('f', '2015'), ('g', '2016'), ('h', '2017'), ('h', '2018'), ('h', '2019')], default='h', max_length=1),
        ),
    ]

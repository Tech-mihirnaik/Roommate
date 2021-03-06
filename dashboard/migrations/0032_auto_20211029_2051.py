# Generated by Django 3.1.4 on 2021-10-29 15:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0031_auto_20211029_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='addroom',
            name='CCTV',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='addroom',
            name='Gym',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='addroom',
            name='Laundry',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='addroom',
            name='Water',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bookingrooms',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 29, 20, 51, 26, 408120)),
        ),
    ]

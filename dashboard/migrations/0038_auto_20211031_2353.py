# Generated by Django 3.1.4 on 2021-10-31 18:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0037_auto_20211031_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingrooms',
            name='timestamp',
            field=models.DateTimeField(default=datetime.date(2021, 10, 31)),
        ),
    ]

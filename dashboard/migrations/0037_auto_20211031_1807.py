# Generated by Django 3.1.4 on 2021-10-31 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0036_auto_20211031_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_link',
            name='gender',
            field=models.CharField(default='UniSex', max_length=20),
        ),
        migrations.AlterField(
            model_name='bookingrooms',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 31, 18, 7, 3, 536471)),
        ),
    ]

# Generated by Django 3.1.4 on 2021-10-31 11:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0034_auto_20211030_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment_link',
            name='token',
        ),
        migrations.AlterField(
            model_name='bookingrooms',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 31, 17, 21, 25, 410704)),
        ),
    ]

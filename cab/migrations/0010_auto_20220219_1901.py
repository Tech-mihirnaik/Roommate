# Generated by Django 3.2.7 on 2022-02-19 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cab', '0009_auto_20220216_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookedcab',
            old_name='payment_mode_200',
            new_name='payment_link',
        ),
        migrations.AlterField(
            model_name='bookedcab',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 19, 19, 1, 8, 926945)),
        ),
    ]

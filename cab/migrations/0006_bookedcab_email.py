# Generated by Django 3.2.8 on 2021-11-01 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cab', '0005_bookedcab_booking_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedcab',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
    ]
# Generated by Django 3.1.4 on 2021-10-19 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20211020_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addroom',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='bookingrooms',
            name='email',
            field=models.CharField(default='null', max_length=50),
        ),
    ]

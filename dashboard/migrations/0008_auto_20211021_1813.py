# Generated by Django 3.1.4 on 2021-10-21 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20211021_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingrooms',
            name='logged_mail',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='bookingrooms',
            name='email',
            field=models.CharField(default='null', max_length=50),
        ),
    ]
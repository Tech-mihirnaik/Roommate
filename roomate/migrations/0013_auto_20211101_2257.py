# Generated by Django 3.2.8 on 2021-11-01 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomate', '0012_auto_20211027_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='dataform',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

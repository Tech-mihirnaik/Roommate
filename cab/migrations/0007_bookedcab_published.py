# Generated by Django 3.2.8 on 2021-11-01 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cab', '0006_bookedcab_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedcab',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]

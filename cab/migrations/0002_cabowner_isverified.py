# Generated by Django 3.2.7 on 2021-10-30 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabowner',
            name='isverified',
            field=models.BooleanField(default=False),
        ),
    ]
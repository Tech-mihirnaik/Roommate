# Generated by Django 3.1.4 on 2021-10-21 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_addroom_room_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addroom',
            name='room_id',
        ),
    ]

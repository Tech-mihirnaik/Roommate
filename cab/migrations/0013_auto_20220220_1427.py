# Generated by Django 3.2.7 on 2022-02-20 08:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cab', '0012_auto_20220220_0132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookedcab',
            old_name='transaction_date_200',
            new_name='transaction_date',
        ),
        migrations.RenameField(
            model_name='bookedcab',
            old_name='transaction_id_200',
            new_name='transaction_id',
        ),
        migrations.AddField(
            model_name='bookedcab',
            name='duepay_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bookedcab',
            name='advpay_link',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='bookedcab',
            name='advpay_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bookedcab',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 20, 14, 27, 9, 460341)),
        ),
        migrations.AlterField(
            model_name='bookedcab',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='driver',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]

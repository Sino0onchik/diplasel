# Generated by Django 5.0.6 on 2024-06-03 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_sitecontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='shop.car'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=123),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 06:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='wishlist',
            field=models.ManyToManyField(blank=True, to='product.Product'),
        ),
    ]
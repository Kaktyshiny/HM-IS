# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-13 14:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internet_shop', '0012_remove_basketitems_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basketitems',
            name='good',
        ),
        migrations.DeleteModel(
            name='BasketItems',
        ),
    ]

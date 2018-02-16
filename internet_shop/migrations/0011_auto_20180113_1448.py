# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-13 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internet_shop', '0010_auto_20180113_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='good',
            name='size',
        ),
        migrations.AddField(
            model_name='basketitems',
            name='good',
            field=models.ManyToManyField(related_name='goods_in_basketss', to='internet_shop.Good'),
        ),
        migrations.RemoveField(
            model_name='good',
            name='color',
        ),
        migrations.AddField(
            model_name='good',
            name='color',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='good_color', to='internet_shop.Colors'),
        ),
        migrations.AddField(
            model_name='good',
            name='sizes',
            field=models.ManyToManyField(related_name='good_sizes', to='internet_shop.Sizes'),
        ),
    ]

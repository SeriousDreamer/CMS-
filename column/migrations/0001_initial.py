# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-03 02:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Columns',
            fields=[
                ('columnId', models.AutoField(primary_key=True, serialize=False, verbose_name='columnId')),
                ('parent', models.IntegerField(default=0, verbose_name='父分类id')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('name', models.CharField(default='0', max_length=100, verbose_name='分类名称')),
            ],
            options={
                'db_table': 'Columns',
            },
        ),
    ]

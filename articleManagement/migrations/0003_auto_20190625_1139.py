# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-25 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleManagement', '0002_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=50, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='article',
            name='column',
            field=models.IntegerField(default=1, verbose_name='分类'),
        ),
        migrations.AlterField(
            model_name='article',
            name='commentId',
            field=models.IntegerField(verbose_name='评论'),
        ),
        migrations.AlterField(
            model_name='article',
            name='commentStatus',
            field=models.BooleanField(verbose_name='是否开启评论'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='文章内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='null', upload_to='static/images', verbose_name='特色图片'),
        ),
        migrations.AlterField(
            model_name='article',
            name='introduction',
            field=models.CharField(max_length=500, verbose_name='摘要'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publicStatus',
            field=models.CharField(max_length=50, verbose_name='发布状态'),
        ),
        migrations.AlterField(
            model_name='article',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50, verbose_name='文章标题'),
        ),
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.TextField(verbose_name='文章url'),
        ),
    ]

from django.db import models


# Create your models here.
class Columns(models.Model):
    columnId = models.AutoField(verbose_name='columnId', primary_key=True)
    parent = models.IntegerField(verbose_name='父分类id', default=0)
    time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    name = models.CharField(verbose_name='分类名称', max_length=100, default='0')

    class Meta:
        db_table = 'Columns'



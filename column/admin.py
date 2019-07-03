from django.contrib import admin
from . import models


# Register your models here.
class ColumnManager(admin.ModelAdmin):
    li = ['columnId', 'parent', 'time', 'name']
    list_display = li
    list_display_links = li


admin.site.register(models.Columns, ColumnManager)

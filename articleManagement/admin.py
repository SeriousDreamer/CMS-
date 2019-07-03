from django.contrib import admin
from . import models


# Register your models here.
class ArticleManager(admin.ModelAdmin):
    li = ['id', 'title', 'author', 'image', 'content',
          'time', 'introduction', 'publicStatus',
          'commentStatus', 'commentId', 'url']
    list_display = li
    list_display_links = li


admin.site.register(models.Article, ArticleManager)

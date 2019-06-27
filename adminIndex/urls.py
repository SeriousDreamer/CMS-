from django.conf.urls import url, include
from . import views
from articleManagement import views as arViews

urlpatterns = [
    url(r'^web/articleList', arViews.show_index),
    url(r'^web/writeArticle', arViews.write_article),
    url(r'^web/updateArticle', arViews.update_article),
    url(r'^$', views.show_index),
]

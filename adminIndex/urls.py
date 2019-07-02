from django.conf.urls import url, include
from . import views
from articleManagement import views as arViews
from column import views as coViews

urlpatterns = [
    url(r'^web/articleList', arViews.show_index),
    url(r'^web/writeArticle', arViews.write_article),
    url(r'^web/updateArticle', arViews.update_article),
]

urlpatterns += [
    url(r'backStage/column', coViews.show_index),
    url(r'backStage/addColumn', coViews.add_column),
]

urlpatterns += [
    url(r'^$', views.show_index),
]

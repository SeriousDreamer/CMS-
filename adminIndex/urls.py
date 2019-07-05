from django.conf.urls import url, include
from . import views
from articleManagement import views as arViews
from column import views as coViews

urlpatterns = [
    url(r'^web/articleList', arViews.show_index),
    url(r'^web/writeArticle', arViews.write_article),
    url(r'^web/updateArticle', arViews.update_article),
    url(r'^web/removeArticleRecycle', arViews.remove_article_recycle),
    url(r'^web/recycleArticle', arViews.recycle_article),
    url(r'^web/deleteArticle', arViews.delete_article),
    url(r'^web/recoverArticle', arViews.recover_article),
    url(r'^web/upload', views.upload, name='api-upload-url'),
]

urlpatterns += [
    url(r'^backStage/column', coViews.show_index),
    url(r'^backStage/addColumn', coViews.add_column),
    url(r'^backStage/deleteColumn', coViews.delete_column),
]

urlpatterns += [
    url(r'^$', views.show_index),
]

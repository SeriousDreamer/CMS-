from django.conf.urls import url, include
from . import views
from articleManagement import views as ar_views
from column import views as co_views
from mediaManagement import views as me_views

urlpatterns = [
    url(r'^web/articleList', ar_views.show_index),
    url(r'^web/writeArticle', ar_views.write_article),
    url(r'^web/updateArticle', ar_views.update_article),
    url(r'^web/removeArticleRecycle', ar_views.remove_article_recycle),
    url(r'^web/recycleArticle', ar_views.recycle_article),
    url(r'^web/deleteArticle', ar_views.delete_article),
    url(r'^web/recoverArticle', ar_views.recover_article),
]

urlpatterns += [
    url(r'^web/mediaList', me_views.media_list, name='get_media_list'),
    url(r'^web/upload', me_views.upload, name='api-upload-url'),
    url(r'^web/delete', me_views.delete),
    # url(r'^web/upsload', me_views.uploads, name="upload"),
]

urlpatterns += [
    url(r'^backStage/column', co_views.show_index),
    url(r'^backStage/addColumn$', co_views.add_column, name='addColumn'),
    url(r'^backStage/deleteColumn', co_views.delete_column),
]

urlpatterns += [
    url(r'^$', views.show_index),
]

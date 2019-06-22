from django.conf.urls import url, include
from . import views
from articleManagement import views as arViews

urlpatterns = [
    url(r'^articleList', arViews.show_index),

]

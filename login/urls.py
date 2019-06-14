from django.conf.urls import url
from . import views, do_login

urlpatterns = [
    url(r'^dologin', do_login.do_login),
    url(r'^create_code/$', views.create_code),
    url(r'', views.show_login)
]

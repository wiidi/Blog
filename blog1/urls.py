from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.showBlogs),
    url(r'^article/(?P<article_id>[1-9][0-9]*)$',views.article_page),
    url(r'^edit/(?P<article_id>[1-9][0-9]*)$',views.edit_page),
    url(r'^edit_action/(?P<article_id>[1-9][0-9]*)$', views.edit_action),
    url(r'^editor/',views.editor),
    url(r'^test/',views.test),
]
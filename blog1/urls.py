from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.showBlogs),
    url(r'^write/',views.writeBlogs),
    url(r'^index/',views.showBlogs),
]
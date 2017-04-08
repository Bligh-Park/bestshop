from django.conf.urls import url
from etcpage import views


urlpatterns = [
    url(r'^$', views.home),
]
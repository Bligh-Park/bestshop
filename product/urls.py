from django.conf.urls import url
from product import views


urlpatterns = [
    url(r'^products$', views.product_list, name='product_list'),
    url(r'^products/(?P<product_id>\d+)$', views.product_detail, name='product_detail'),
]
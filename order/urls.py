from django.conf.urls import url
from order import views

urlpatterns = [
    url(r'^order$', views.order, name='order_order'),
    url(r'^order/create-order$', views.order_create_order, name='order_create_order'),
    url(r'^order/complete$', views.order_complete, name='order_complete'),

]

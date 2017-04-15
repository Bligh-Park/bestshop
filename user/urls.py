from django.conf.urls import url
from user import views


urlpatterns = [
    url(r'^login$', views.login_page),
    url(r'^mypage/cart$', views.mypage_cart, name='user_mypage_cart'),
]
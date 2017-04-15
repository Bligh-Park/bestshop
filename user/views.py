from django.db.models import F
from django.shortcuts import render

from order.models import Cart
from product.models import Product


def login_page(request):
    return render(request, 'user/login.html')


def mypage_cart(request):
    # http://naver.com/?id=3&id=4&id=5
    if request.method == 'POST':
        cart, is_created = Cart.objects.get_or_create(
            userinfo=request.user.userinfo,
            product=Product.objects.get(id=request.POST.get('product_id')),
            defaults={
                'count': request.POST.get('count')
            }
        )

        if not is_created:
            # update cart set count = count + 1 where id=~~
            cart.count = F('count') + int(request.POST.get('count'))
            # update cart set count = 2 where id=~~
            # cart.count = cart.count + 1
            cart.save()
            cart.refresh_from_db()

        """
        Cart.objects.create(
            userinfo=request.user.userinfo,
            product=Product.objects.get(id=request.POST.get('product_id')),
            count=request.POST.get('count')
        )
        """
    return render(request, 'user/mypage/cart.html')
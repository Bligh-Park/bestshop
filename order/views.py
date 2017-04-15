from django.http import Http404, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_POST

from order.models import Cart, Order, OrderProductItem


@require_POST
def order(request):
    cart = Cart.objects.filter(
        id__in=request.POST.getlist('cart'),
        userinfo=request.user.userinfo
    )

    return render(request, 'order/order.html', context={
        'cart': cart
    })


@require_POST
def order_create_order(request):
    cart = Cart.objects.filter(
        id__in=request.POST.getlist('cart'),
        userinfo=request.user.userinfo
    )

    order = Order.objects.create(
        userinfo=request.user.userinfo,
        delivery_fee=0,
        point=0,
        amount=sum(item.product.price * item.count for item in cart),
        postcode=request.POST.get('postcode'),
        address_1=request.POST.get('address_1'),
        address_2=request.POST.get('address_2'),
        name=request.POST.get('name')
    )

    for item in cart:
        # TODO 최적화
        OrderProductItem.objects.create(
            order=order,
            product=item.product,
            count=item.count,
            point=0,
            discount=0,
            amount=item.product.price * item.count
        )

    return JsonResponse({
        'order_id': order.id,
        'name': order.subject,
        'amount': order.amount,
        'buyer_name': order.name,
        'buyer_addr': ' '.join([order.address_1, order.address_2]),
        'buyer_postcode': order.postcode
    })


def order_complete(request):
    return render(request, 'order/complete.html')

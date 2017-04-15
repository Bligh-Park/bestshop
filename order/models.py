from django.db import models

# Create your models here.
class Cart(models.Model):
    userinfo = models.ForeignKey('user.UserInfo')
    product = models.ForeignKey('product.Product')
    count = models.IntegerField()

    # 나중에 카트에 있는 상품을 추가했을 때 기존 상품 카운트를 올리기 위해 작업
    # unique 를 걸어줘야 함
    class Meta:
        unique_together = (
            ('userinfo', 'product'),
        )


class Order(models.Model):
    userinfo = models.ForeignKey('user.UserInfo')
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_fee = models.IntegerField()
    point = models.IntegerField()
    amount = models.IntegerField()
    tid = models.CharField(max_length=128, null=True)
    state = models.IntegerField()
    postcode = models.CharField(max_length=5)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128)
    name = models.CharField(max_length=64)


class OrderProductItem(models.Model):
    order = models.ForeignKey('Order')
    product = models.ForeignKey('product.Product')
    count = models.IntegerField()
    point = models.IntegerField()
    discount = models.IntegerField()
    amount = models.IntegerField()
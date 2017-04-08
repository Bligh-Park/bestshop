from django.db import models

# Create your models here.
class Cart(models.Model):
    userinfo = models.ForeignKey('user.UserInfo')
    product = models.ForeignKey('product.Product')
    count = models.IntegerField()


class Order(models.Model):
    userinfo = models.ForeignKey('user.UserInfo')
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_fee = models.IntegerField()
    point = models.IntegerField()
    amount = models.IntegerField()
    tid = models.CharField(max_length=128)
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
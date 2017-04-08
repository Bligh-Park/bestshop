from django.db import models

# Create your models here.
class UserLevel(models.Model):
    min_point = models.IntegerField()
    name = models.CharField(max_length=64)
    point_rate = models.FloatField()


class UserInfo(models.Model):
    user = models.OneToOneField(User)
    birthday = models.DateField()
    phone = PhoneNumberField()
    gender = models.CharField(max_length=1)
    postcode = models.CharField(max_length=5)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    point = models.IntegerField()
    level = models.ForeignKey('UserLevel')
    wishlist = models.ManyToManyField('product.Product')
    class Meta:
        unique_together = (
                   ('phone', )
        )


class PointHistory(models.Model):
    userinfo = models.ForeignKey(UserInfo)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    delta = models.IntegerField()



from django.db import models

# Create your models here.
class Review(models.Model):
    author = models.ForeignKey('user.UserInfo')
    product = models.ForeignKey('product.Product')
    created_at = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()
    message = models.TextField()



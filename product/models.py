from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)
    parent = models.ForeignKey('self', null=True)
    priority = models.IntegerField()

    class Meta:
        index_together = (
            ('parent', 'priority'),
        )


class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    image = models.ImageField()
    description = models.TextField()
    inventory_count = models.IntegerField()
    score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category')


class DateRangeDiscount(models.Model):
    category = models.ForeignKey('Category')
    start = models.DateTimeField()
    end = models.DateTimeField()
    rate = models.FloatField()
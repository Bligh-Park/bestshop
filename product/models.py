from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='parent_set')
    priority = models.IntegerField()

    class Meta:
        index_together = (
            ('parent', 'priority'),
        )

    @property
    def all_parent_set(self):
        all_parent_set_list=[self]

        for category in self.parent_set.all():
            all_parent_set_list.extend(category.all_parent_set)

        return all_parent_set_list

    def __str__(self):
        return '%d. %s' % (self.id, self.name)


class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    image = models.ImageField()
    description = models.TextField()
    inventory_count = models.IntegerField()
    score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category')

    def __str__(self):
        return '%d. %s' % (self.id, self.name)


class DateRangeDiscount(models.Model):
    category = models.ForeignKey('Category')
    start = models.DateTimeField()
    end = models.DateTimeField()
    rate = models.FloatField()
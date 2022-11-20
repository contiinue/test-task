from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Item(models.Model):
    """ Model for items """
    currencies = (
        ('rub', 'Ruble'),
        ('usd', 'Dollar'),
    )

    name = models.CharField(max_length=63)
    description = models.TextField(null=True)
    price = models.IntegerField(default=1)
    currency = models.CharField(choices=currencies, max_length=20)
    discount = models.ForeignKey('Discount', on_delete=models.PROTECT, null=True)

    def get_discount(self):
        return self.price - (self.price / 100 * self.discount.discount) if self.discount else self.price

    def __str__(self):
        return self.name


class Order(models.Model):
    """  """
    items = models.ManyToManyField(Item)


class Discount(models.Model):
    """ Model for sale """
    discount = models.IntegerField(validators=[
        MaxValueValidator(100),
        MinValueValidator(1)
    ])

    def __str__(self):
        return f'{self.discount}%'

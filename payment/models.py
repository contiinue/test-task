from django.db import models


class Item(models.Model):
    """ Model for items """
    name = models.CharField(max_length=63)
    description = models.TextField(null=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

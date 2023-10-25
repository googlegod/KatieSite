from django.db import models


class ShopItem(models.Model):
    DROPDOWN_SELECTION = (
        ('cup', 'Cups'),
        ('decoration', 'Decorations'),
        ('shirt', 'Shirts'),

    )

    image = models.ImageField(upload_to='static/images/shop')
    name = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True)
    price = models.FloatField(default=0)
    category = models.CharField(max_length=10, choices=DROPDOWN_SELECTION, default='')
    inventory = models.IntegerField(default=0)
    sku = models.CharField(default='', blank=True, max_length=10, unique=True)

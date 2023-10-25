from django.db import models


# Create your models here.
class GalleryItem(models.Model):
    img = models.ImageField(upload_to='static/images/gallery')
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50)
    price = models.FloatField(default=0, blank=True, null=True)


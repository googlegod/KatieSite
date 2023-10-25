from django.db import models


class CarouselImage(models.Model):
    image = models.ImageField(upload_to='static/images/carousel')
# Create your models here.

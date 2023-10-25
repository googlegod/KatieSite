from django.shortcuts import render
from .models import CarouselImage


def index(request):
    images = CarouselImage.objects.all()
    first = images[0]

    context = {'images': images, 'first': first}

    return render(request, 'base/index.html', context)
# Create your views here.

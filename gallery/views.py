from django.shortcuts import render
from django.http import HttpResponse
from .models import GalleryItem


def index(request):
    items = GalleryItem.objects.all()
    context = {'items': items}

    return render(request, 'gallery/gallery_main.html', context)


def cups(request):
    return HttpResponse("Cups")
# Create your views here.

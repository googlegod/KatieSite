from django.shortcuts import render
from django.http import HttpResponse
from .models import ShopItem


def index(request):
    return render(request, 'shop/index.html')


def cups(request):
    items = ShopItem.objects.filter(category='cup')
    context = {'items': items}
    return render(request, 'shop/cups.html', context)


def decorations(request):
    items = ShopItem.objects.filter(category='decoration')
    context = {'items': items}
    return render(request, 'shop/cups.html', context)

def featured(request):
    items = ShopItem.objects.filter(category='featured')
    context = {'items':items}
    return render()
# Create your views here.

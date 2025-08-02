from django.shortcuts import render
from items.models import Category, Item


def home(request):
    items = Item.objects.all()
    return render(request, 'core/home.html', {'items': items})

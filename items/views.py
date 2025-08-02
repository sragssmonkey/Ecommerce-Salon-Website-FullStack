from django.shortcuts import render
from django.shortcuts import redirect,get_object_or_404
from .models import Item, cart
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

def remove_from_cart(request, item_id):
    if request.user.is_authenticated:
        cart.objects.filter(user=request.user, id=item_id).delete()
    return redirect('cart')

def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        item= get_object_or_404(Item,id=product_id)
        cart_item , created= cart.objects.get_or_create(user=request.user, thing=item)

        if not created:
            cart_item.quantity += 1
            cart_item.save()
        
        return redirect('cart')
    else:
        return redirect('login')

@login_required(login_url='login') 
def cartview(request):
    cart_items=cart.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'items/cart.html', {'cart_items': cart_items, 'total': total})
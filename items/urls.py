from django.urls import path
from . import views
from .views import cartview,add_to_cart,remove_from_cart

urlpatterns=[
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cartview, name='cart'),
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('basket', views.basket, name='basket'),
    path('checkout', views.checkout, name='checkout'),
    path('wishlist', views.wishlist, name='wishlist'),
]

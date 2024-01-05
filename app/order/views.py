from django.shortcuts import render
from product.models import ProductItem

from order.models import Order, WishList


def basket(request):
    context = {
        'items': ProductItem.objects.filter(user=request.user, status=0)
    }
    return render(request, 'order/basket.html', context)


def checkout(request):
    context = {
        'order': Order.objects.get(user=request.user, is_done=False)
    }
    return render(request, 'order/checkout.html', context)


def wishlist(request):
    wishlist = WishList.objects.filter(user=request.user).first()
    context = {
        'wishlist': wishlist
    }
    return render(request, 'order/wishlist.html', context)

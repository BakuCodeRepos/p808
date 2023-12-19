from django.shortcuts import render
from product.models import ProductItem


def basket(request):
    context = {
        'items': ProductItem.objects.filter(user=request.user, status=0)
    }
    return render(request, 'order/basket.html', context)

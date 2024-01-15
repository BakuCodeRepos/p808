from django.shortcuts import render
from product.models import Category, Product


def index(request):
    categories = Category.objects.filter(is_parent=True).prefetch_related('products')
    trandy_products = Product.objects.all().order_by('-adding_to_basket_count')[:8]
    just_arrived_products = Product.objects.all().order_by('-created_at')[:8]

    context = {
        'categories': categories,
        'trandy_products': trandy_products,
        'just_arrived_products': just_arrived_products
    }
    return render(request, 'home/index.html', context)

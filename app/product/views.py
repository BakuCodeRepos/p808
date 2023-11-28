from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Category, Product


class ProductListView(generic.ListView):
    template_name = 'product/list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 9


def products_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {
        'products': products
    }
    return render(request, 'product/list.html', context)


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
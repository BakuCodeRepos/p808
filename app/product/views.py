from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic

from .forms import CommentForm
from .models import Category, Comment, Product


class ProductListView(generic.ListView):
    template_name = "product/list.html"
    model = Product
    context_object_name = "products"
    paginate_by = 9


def products_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {"products": products}
    return render(request, "product/list.html", context)


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    other_products = Product.objects.filter(category=product.category).exclude(
        slug=product.slug
    ).distinct()

    reviews = Comment.objects.filter(product=product).order_by('-created_at')
    review_count = reviews.count()
    form = CommentForm()


    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.product = product
            form.save()
            return redirect(reverse("product-detail", args=(product.slug,)))

        
    context = {
        "product": product,
        'other_products': other_products,
        'form': form,
        'reviews': reviews,
        'review_count': review_count,
        }
    return render(request, "product/detail.html", context)


def search(request):
    query = request.GET.get('search')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {
        'result_count': len(products),
        'query': query,
        'results': products
    }

    return render(request, 'product/search.html', context)
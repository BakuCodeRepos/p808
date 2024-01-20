from typing import Any

from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views import generic

from .forms import CommentForm
from .models import Category, Comment, Product


class ProductListView(generic.ListView):
    template_name = "product/list.html"
    model = Product
    context_object_name = "products"
    paginate_by = 9

    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()
        print('heyooo============', self.request.GET)
        if 'filter' in self.request.GET:
            our_filter = self.request.GET['filter']
            if our_filter == 'latest':
                qs = qs.order_by('-created_at')
            elif our_filter == 'trandy':
                qs = qs.order_by('-adding_to_basket_count')
            elif our_filter == 'increased_price':
                qs = qs.order_by('price')
            elif our_filter == 'decreased_price':
                qs = qs.order_by('-price')
        if 'start_price' in self.request.GET and 'end_price' in self.request.GET:
            start_price = int(self.request.GET.get('start_price'))
            end_price = int(self.request.GET.get('end_price'))
            qs = qs.filter(price__range=[start_price, end_price])
        return qs
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        if 'start_price' in self.request.GET and 'end_price' in self.request.GET:
            start_price = int(self.request.GET.get('start_price'))
            end_price = int(self.request.GET.get('end_price'))
            context['start_price'] = start_price
            context['end_price'] = end_price
        if 'filter' in self.request.GET:
            our_filter = self.request.GET['filter']
            if our_filter == 'latest':
                context['our_filter'] = _('Latest')
            elif our_filter == 'trandy':
                context['our_filter'] = _('Popularity')
            elif our_filter == 'increased_price':
                context['our_filter'] = _('Increased price')
            elif our_filter == 'decreased_price':
                context['our_filter'] = _('Decreased price')
        else:
            context['our_filter'] = _('Sort by')
        return context


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
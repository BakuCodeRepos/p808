from django.shortcuts import render


def product_list(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'product/list.html', context)

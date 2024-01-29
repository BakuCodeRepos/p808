from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils.translation import gettext as _
from django.core.mail import send_mail
from account.models import SubscribedUser
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


def subscribe(request):
    email = request.POST.get('subscribed_user')

    if request.user.is_authenticated:
        if request.user.email == email:
            if not SubscribedUser.objects.filter(email=email).first():
                SubscribedUser.objects.create(email=email)
                messages.success(request, _('Congratulations! You have subscribed successfully!'))
                # send_mail(
                #     'Subscription',
                #     'Congratulations! You have subscribed successfully!',
                #     'notificationtodo@gmail.com',
                #     [request.user.email]
                # )
                return redirect('/')
            else:
                messages.error(request, _('Ooops! You have subscribed already!'))
                return redirect('/')
        else:
            messages.error(request, _("Ooops! This email doesn't belong to you!"))
            return redirect('/')
    else:
        messages.error(request, _("Looks like you are not logged in, please log in to subscribe"))
    return redirect('/')

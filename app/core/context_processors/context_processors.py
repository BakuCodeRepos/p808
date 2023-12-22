from product.models import Category, ProductItem
from contact.models import ContactInfo


def subject_renderer(request):
    context = {
        'context_categories': Category.objects.filter(is_parent=True),
        'context_contact': ContactInfo.objects.first()
    }
    if request.user.is_authenticated:
        context.update({
            'basket_order_count': ProductItem.objects.filter(user=request.user, status=0).count() or 0,
            # 'wish_list_count': WishList.objects.filter(user=request.user).first().product.count() if WishList.objects.filter(user=request.user).first() else 0
            })
    return context

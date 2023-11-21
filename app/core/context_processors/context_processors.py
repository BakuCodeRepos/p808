from product.models import Category
from contact.models import ContactInfo


def subject_renderer(request):
    context = {
        'context_categories': Category.objects.filter(is_parent=True),
        'context_contact': ContactInfo.objects.first()
    }
    return context

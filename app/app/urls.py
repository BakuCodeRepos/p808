from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', include('core.urls')),
    path('', include('account.urls')),
    path("", include("about.urls")),
    path("", include("contact.urls")),
    path('', include('product.urls')),
    path('', include('order.urls')),
    path('product-api/', include('product.api.urls')),
    path('order-api/', include('order.api.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path

from . import views

urlpatterns = [
    path('products', views.ProductListView.as_view(), name='products'),
    path('products/categories/<slug:category_slug>', views.products_by_category, name='products-by-category'),
    path('products/<slug:product_slug>', views.product_detail, name='product-detail')
]

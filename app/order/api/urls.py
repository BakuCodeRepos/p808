from django.urls import path

from . import views

urlpatterns = [
    path('delete-product-item/<int:id>', views.ProductItemDeleteAPIView.as_view(), name='delete-product-item'),
]

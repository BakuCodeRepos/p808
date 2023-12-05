from django.urls import path

from . import views

urlpatterns = [
    path('create-product-item', views.ProductItemCreateAPIView.as_view(), name='create-product-item'),
]

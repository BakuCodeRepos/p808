from django.urls import path

from . import views

urlpatterns = [
    path('delete-product-item/<int:id>', views.ProductItemDeleteAPIView.as_view(), name='delete-product-item'),
    path('create-order', views.OrderCreateAPIView.as_view(), name='create-order'),
    path(
        "orders/is-done/<int:id>",
        views.OrderIsDoneAPIView.as_view(),
        name="order-is-done",
    ),
]

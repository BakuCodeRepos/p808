from rest_framework import generics
from product.api.serializers import ProductItemSerializer
from product.models import ProductItem


class ProductItemDeleteAPIView(generics.DestroyAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer
    lookup_field = 'id'

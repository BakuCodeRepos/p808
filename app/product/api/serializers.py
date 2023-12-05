from rest_framework import serializers
from ..models import ProductItem


class ProductItemSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = ProductItem
        fields = ['product', 'size', 'color', 'quantity']

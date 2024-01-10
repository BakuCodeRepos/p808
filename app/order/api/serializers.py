from rest_framework import serializers
from ..models import Order, WishList


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Order
        exclude = ('is_done',)


class OrderIsDoneSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ('is_done',)


class AddToWishListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WishList
        fields = ('product',)
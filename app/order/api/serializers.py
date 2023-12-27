from rest_framework import serializers
from ..models import Order


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Order
        exclude = ('is_done',)

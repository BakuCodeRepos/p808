from rest_framework import generics
from product.api.serializers import ProductItemSerializer
from product.models import ProductItem
from ..models import Order
from .serializers import OrderSerializer
from rest_framework.response import Response
import json


class ProductItemDeleteAPIView(generics.DestroyAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer
    lookup_field = 'id'


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        data = serializer.data
        # data['absolute_url'] = request.build_absolute_uri(reverse("checkout"))
        Order.objects.filter(user=request.user, is_done=False).exclude(id=instance.id).delete()
        if items := json.loads(request.data.get('items', '[]')):
            for item in items: # [2, 4, 11]
                print('item', item)
                if item is not None:
                    obj = ProductItem.objects.get(
                        id=int(item),
                    )
                    obj.order = instance
                    obj.save()
                    # instance.items.add(obj)

        return Response({"detail": "OK", 'data': data}, status=201)

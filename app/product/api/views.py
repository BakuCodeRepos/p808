from rest_framework import generics
from rest_framework.response import Response

from ..models import ProductItem
from .serializers import ProductItemSerializer


class ProductItemCreateAPIView(generics.CreateAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        instance.user = request.user
        instance.save()
        

        data = serializer.data

        return Response(data={"detail": "OK", 'data': data}, status=201)

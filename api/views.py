from .serializers import *
from accounts.models import *
from rest_framework import viewsets

class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
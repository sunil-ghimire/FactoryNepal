from rest_framework import serializers
from accounts.models import *


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        exclude = ('password',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

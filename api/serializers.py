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


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class CreateSellerSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(max_length=100, required=True)
    class Meta:
        model = Seller
        fields = ('email', 'password','company_name','company_address','company_phone')

    def create(self, validated_data):
        seller = Seller.objects.create_user(**validated_data)
        seller.user_type = 'seller'
        seller.save()
        return seller

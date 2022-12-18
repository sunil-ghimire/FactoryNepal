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
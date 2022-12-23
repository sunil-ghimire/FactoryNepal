from rest_framework import serializers
from accounts.models import *
from rest_framework.response import Response


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        exclude = ('password',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        lookup_field = 'name'
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
        fields = ('email', 'password', 'company_name',
                  'company_address', 'company_phone')

    def create(self, validated_data):
        seller = Seller.objects.create_user(**validated_data)
        seller.user_type = 'seller'
        seller.save()
        return seller


class SpecificSellerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'image', 'description',
                  'seller', 'category', 'sub_category', 'slug')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class ProductCategorySerailizer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ('name',)
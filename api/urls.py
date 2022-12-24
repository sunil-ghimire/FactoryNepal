from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('sellers', SellerViewSet, basename='sellers')
router.register('products', ProductViewSet, basename='products')
router.register('product-category',ProductCategoryViewSet, basename='product-category')
router.register('product-sub-category',ProductSubCategoryViewSet, basename='product-sub-category')

urlpatterns = [
    path('', include(router.urls)),
    path('create_user/', create_user, name='create_user'),
    path('login_user/', login_user, name='login_user'),

    path('create_seller/', create_seller, name='create_seller'),

    path('specific_seller_products/<int:pk>/',
         specific_seller_products, name='specific_seller_products'),
]

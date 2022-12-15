from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('company/', views.company, name='company'),
    path('product/', views.product, name='product'),

    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('seller/register/', views.seller_register_page, name='seller_register'),

    path('dashboard/', views.dashboard, name='seller_dashboard'),
    path('add-product/', views.add_product, name='seller_product'),
    path('add-product-category/', views.add_product_category, name='seller_product_category'),
    path('add-product-sub-category/', views.add_product_sub_category, name='seller_product_sub_category'),
]

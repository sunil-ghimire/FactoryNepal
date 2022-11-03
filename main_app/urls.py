from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('company/', views.company, name='company'),
    path('product/', views.product, name='product'),
    path('seller/signup/', views.seller_signup, name='seller_signup'),
    path('seller/login/',views.seller_login, name="seller_login"),
    path('seller/logout/', views.seller_logout,name="seller_logout"),


    #normal user
    path('login/', views.user_login, name='user_login'),

]

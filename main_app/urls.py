from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('company/', views.company, name='company'),
    path('product/', views.product, name='product'),
]

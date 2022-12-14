from django import forms
from accounts.models import Seller, User, Product, ProductCategory, ProductSubCategory
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'full_name']


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class SellerSingupForm(UserCreationForm):
    user_type = forms.CharField(widget=forms.HiddenInput(), initial='seller')

    class Meta:
        model = Seller
        fields = ['email', 'password1', 'password2', 'company_name', 'company_description',
                  'company_address', 'company_logo', 'company_phone', "user_type"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','description','image','sub_category']


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name']

class ProductSubCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductSubCategory
        fields = ['name','category']
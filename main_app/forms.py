from django import forms
from accounts.models import *

class SellerSignupForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['company_name', 'company_description', 'company_address','company_phone', 'company_email', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'id': 'seller_password'
            }),
        }

class SellerSignForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['company_email', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'id': 'seller_password'
            }),
        }

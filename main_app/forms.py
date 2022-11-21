from django import forms
from accounts.models import Seller, User
from django.contrib.auth.hashers import make_password


class SellerSingupForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['email', 'password', 'company_name', 'company_owner_name', 'company_description', 'company_address', 'company_phone', 'company_logo', 'website', 'facebook', 'instagram', 'twitter', 'youtube',
                  'number_of_employee', 'company_type', 'company_size', 'company_banner', 'company_location', 'company_state', 'company_city', 'company_zip', 'company_established', 'company_pan_number', 'company_pan_document']


# user section start here
class UserSignupForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].required=True

    class Meta:
        model = User
        fields = ['email', 'password', 'full_name']
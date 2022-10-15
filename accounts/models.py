from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    full_name = models.CharField(max_length=100, blank=False)
    password2 = models.CharField(max_length=100, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Seller(models.Model):
    company_name = models.CharField(max_length=100, blank=False)
    comapny_address = models.CharField(max_length=200, blank=False)
    company_phone = models.CharField(max_length=20, blank=False)
    company_email = models.EmailField(blank=False)
    password = models.CharField(max_length=100, blank=False)
    password2 = models.CharField(max_length=100, blank=True)

    website = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    youtube = models.CharField(max_length=100, blank=True)
    number_of_employee = models.CharField(max_length=100, blank=True)

    company_type = models.CharField(max_length=100, blank=True)
    company_size = models.CharField(max_length=100, blank=True)
    company_description = models.TextField(blank=True)
    company_logo = models.ImageField(upload_to='images/', blank=True)
    company_banner = models.ImageField(upload_to='images/', blank=True)
    company_location = models.CharField(max_length=100, blank=True)
    company_country = models.CharField(max_length=100, blank=True)
    company_state = models.CharField(max_length=100, blank=True)
    company_city = models.CharField(max_length=100, blank=True)
    company_zip = models.CharField(max_length=100, blank=True)
    company_latitude = models.CharField(max_length=100, blank=True)
    company_longitude = models.CharField(max_length=100, blank=True)
    company_established = models.CharField(max_length=100, blank=True)
    company_pan_number = models.CharField(max_length=100, blank=True)
    company_pan_document = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

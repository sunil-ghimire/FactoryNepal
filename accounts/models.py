# Create your models here.
from wsgiref.validate import validator
from xml.dom import ValidationErr
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.contrib.auth.hashers import make_password

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
    company_owner_name = models.CharField(max_length=100, blank=False)
    company_address = models.CharField(max_length=200, blank=False)
    company_phone = models.CharField(max_length=20, blank=False)
    company_email = models.EmailField(blank=False)
    password = models.CharField(max_length=100, blank=False)

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
    slug = models.SlugField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if len(self.password) > 5:
            self.password = make_password(self.password)
        else:
            raise ValidationErr('Password length must be greater than 5')

        self.slug = slugify(self.company_name)
        super(Seller, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Sellers'

    def __str__(self):
        return self.company_name


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.name


class ProductSubCategory(models.Model):
    name = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductSubCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Product Sub Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField(null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, null=True, blank=True)
    sub_category = models.ForeignKey(
        ProductSubCategory, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    is_admin_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

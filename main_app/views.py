from django.shortcuts import render, redirect
from django.db.models import Q, Sum
from accounts.models import *
from .forms import *
from django.contrib.auth import logout, get_user_model
from django.contrib.auth import authenticate, login
from .send_email import send_email
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import random
# Create your views here.

User = get_user_model()


def homepage(request):
    if request.method == "POST":
        name = request.POST.get('search')
        product_list = Product.objects.filter(Q(name__icontains=name) | Q(
            description__icontains=name) | Q(price__icontains=name))
        seller_list = Seller.objects.filter(Q(company_name__icontains=name) | Q(
            company_description__icontains=name) | Q(company_address__icontains=name))
        context = {
            'product_lists': product_list,
            'seller_lists': seller_list,
        }
        return render(request, 'main_app/search.html', context=context)
    return render(request, 'main_app/homepage.html')


def company(request):
    if request.method == "GET":
        company_list = Seller.objects.filter(is_admin_approved=True)
        context = {
            'seller_lists': company_list,
        }
        return render(request, 'main_app/company.html', context=context)
    elif request.method == "POST":
        name = request.POST.get('company_search')
        company_list = Seller.objects.filter(Q(company_name__icontains=name) | Q(
            company_description__icontains=name) | Q(company_address__icontains=name))
        context = {
            'seller_lists': company_list,
        }
        return render(request, 'main_app/company.html', context=context)


def company_detail(request, pk):
    seller = Seller.objects.get(id=pk)
    context = {
        'seller': seller,
    }
    return render(request, 'main_app/company_detail.html', context=context)


def product(request):
    if request.method == "GET":
        product_list = Product.objects.filter(is_admin_approved=True)
        context = {
            'product_lists': product_list,
        }
        return render(request, 'main_app/product.html', context=context)
    elif request.method == "POST":
        name = request.POST.get('product_search')
        product_list = Product.objects.filter(Q(name__icontains=name) | Q(
            description__icontains=name) | Q(price__icontains=name))
        context = {
            'product_lists': product_list,
        }
        return render(request, 'main_app/product.html', context=context)


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product,
    }
    return render(request, 'main_app/product_detail.html', context=context)


def register_page(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'main_app/user_signup.html', context)


def login_page(request):
    form = UserLoginForm()
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
    context = {'form': form}
    return render(request, 'main_app/user_login.html', context)


def logout_user(request):
    logout(request)
    return redirect('homepage')


def reset_password(request):
    if request.method == "POST":
        email = request.POST.get('reset-password')
        user = User.objects.filter(email=email).first()
        if user:
            # send email
            uidb64 = urlsafe_base64_encode((user.email).encode())
            body = f"""
            Please click on the link below to reset your password:
            http://localhost:8000/password-reset-confirm/{uidb64}/{user.token}/
            """
            send_email("sunilnp105@gmail.com", body)
            return redirect('reset_password_sent')
    return render(request, 'main_app/reset_password.html', {})


def reset_password_confirm(request, uidb64, token):
    uidb64 = urlsafe_base64_decode(uidb64).decode()
    user = User.objects.filter(email=uidb64).first()
    if user and user.token == token:
        if request.method == "POST":
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 == password2:
                user.set_password(password1)
                user.token = random.randint(100000, 9999999999)
                user.save()
                return redirect('login')
            else:
                uidb64 = urlsafe_base64_encode((user.email).encode())
                return redirect('reset_password_confirm', uidb64=uidb64, token=token)
        return render(request, 'main_app/reset_password_confirm.html', {})
    return render(request, 'main_app/reset_password_confirm.html', {})


def reset_password_sent(request):
    return render(request, 'main_app/reset_password_sent.html', {})


def seller_register_page(request):
    form = SellerSingupForm()

    if request.method == "POST":
        form = SellerSingupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'main_app/seller_signup.html', {'form': form})

    context = {'form': form}
    return render(request, 'main_app/seller_signup.html', context)


def dashboard(request):
    user = request.user
    products = Product.objects.filter(seller=user)
    totol_price = Product.objects.all().aggregate(Sum('price'))
    context = {
        'products': products,
        'total_price': totol_price['price__sum'],
    }
    return render(request, 'main_app/dashboard.html', context=context)


def add_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('seller_dashboard')
    context = {'form': form}
    return render(request, 'main_app/add_product.html', context)


def add_product_category(request):
    form = ProductCategoryForm()
    if request.method == "POST":
        form = ProductCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seller_dashboard')
    context = {'form': form}
    return render(request, 'main_app/add_product_category.html', context)


def add_product_sub_category(request):
    form = ProductSubCategoryForm()
    if request.method == "POST":
        form = ProductSubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seller_dashboard')
    context = {'form': form}
    return render(request, 'main_app/add_product_sub_category.html', context)

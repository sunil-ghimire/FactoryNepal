from django.shortcuts import render, redirect
from django.db.models import Q
from accounts.models import *
from .forms import *
from django.contrib.auth import logout, get_user_model
from django.contrib.auth import authenticate, login
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
        company_list = Seller.objects.all()
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


def product(request):
    if request.method == "GET":
        product_list = Product.objects.all()
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
    return render(request, 'main_app/dashboard.html')
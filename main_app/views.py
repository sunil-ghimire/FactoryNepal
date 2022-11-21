from django.shortcuts import render, redirect
from django.db.models import Q
from accounts.models import *
from .forms import *
from django.contrib.auth import logout, get_user_model
from .forms import SellerSingupForm
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


def seller_signup(request):
    if request.method == "GET":
        form = SellerSingupForm()
        context = {
            'form': form,
        }
        return render(request, 'main_app/seller_signup.html', context=context)
    elif request.method == "POST":
        form = SellerSingupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            return render(request, 'main_app/seller_signup.html', {'form': form})



def seller_logout(request):
    logout(request)
    return redirect('main_app/homepage')




#user section start here
def user_signup(request):
    if request.method == "GET":
        form = UserSignupForm()
        context = {
            'form': form,
        }
        return render(request, 'main_app/user_signup.html', context=context)
    elif request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            return render(request, 'main_app/user_signup.html', {'form': form})
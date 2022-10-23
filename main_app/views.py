from django.shortcuts import render,redirect
from django.db.models import Q
from accounts.models import *

# Create your views here.


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
    if request.method == "POST":
        company_name = request.POST.get('company_name')
        company_owner_name = request.POST.get('company_owner_name')
        company_description = request.POST.get('company_description',None)
        company_address = request.POST.get('company_address')
        company_email = request.POST.get('company_email')
        password = request.POST.get('password')
        company_phone = request.POST.get('company_phone')
        company_website = request.POST.get('company_website',None)
        company_logo = request.FILES.get('company_logo')
        company_banner = request.FILES.get('company_banner')

        seller = Seller(company_name=company_name, company_owner_name = company_owner_name,company_description=company_description, company_address=company_address, company_email=company_email, company_phone=company_phone, company_website=company_website, password=password, company_logo=company_logo, company_banner=company_banner)
        seller.save()
        return redirect('seller_login')
    return render(request, 'main_app/seller_signup.html')

def seller_login(request):
    if request.method == "POST":
        company_email = request.POST.get('company_email')
        password = request.POST.get('password')
        seller = Seller.objects.filter(company_email=company_email, password=password)
        if seller:
            return redirect('seller_dashboard')
        else:
            return redirect('seller_login')
    return render(request, 'main_app/seller_login.html')
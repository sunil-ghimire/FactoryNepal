from django.shortcuts import render
from django.db.models import Q
from accounts.models import *
from itertools import chain

# Create your views here.


def homepage(request):
    if request.method == "POST":
        name = request.POST.get('search')
        product_list = Product.objects.filter(Q(name__icontains=name) | Q(description__icontains=name) | Q(price__icontains=name))
        seller_list = Seller.objects.filter(Q(company_name__icontains=name) | Q(company_description__icontains=name) | Q(company_address__icontains=name))
        results = list(chain(product_list, seller_list))
        for result in results:
            print(result)
        return render(request, 'main_app/search.html', {'results': results})
    return render(request, 'main_app/homepage.html')


def search(request):
    if request.method == "POST":
        pass
    else:
        return render(request, 'main_app/search.html')
from django.shortcuts import render

from accounts.models import Product

# Create your views here.


def homepage(request):
    if request.method == "POST":
        product_name = request.POST.get('myform')
        try:
            name_lists = Product.objects.filter(name__icontains=product_name)
            return render(request, "accounts/homepage.html", {"name_lists": name_lists})
        except Product.DoesNotExist:
            return render(request, "accounts/homepage.html", {'name_lists': name_lists})
    return render(request, 'accounts/homepage.html')


def search(request):
    if request.GET.get('myform'):  # write your form name here
        product_name = request.GET.get('myform')
        try:
            name_lists = Product.objects.filter(name__icontains=product_name)
            return render(request, "search.html", {"name_lists": name_lists})
        except:
            return render(request, "search.html", {'name_lists': name_lists})
    else:
        return render(request, 'search.html', {'name_lists':name_lists})
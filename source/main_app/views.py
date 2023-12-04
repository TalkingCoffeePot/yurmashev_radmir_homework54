from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from main_app.models import Product, Categories
# Create your views here.


def products_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    print(products)
    return render(request, 'main_page.html', context)

#############################################################################
def product_add_view(request):
    categories = Categories.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'add_product.html', context)

#############################################################################
def added_producy_view(request):
    title = request.POST.get('title')  
    price = request.POST.get('price')  
    image = request.POST.get('image')  
    category = request.POST.get('category')  
    description = request.POST.get('description')  

    product = Product.objects.create(title=title, price=price, image=image, category=category, description=description)
    product.save()
    
    return redirect('product_card', pk=product.pk)

# ##############################################################################
def product_view(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'detailed_view.html', context)

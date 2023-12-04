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

def product_add_view(request):
    if request.method == 'GET':
        categories = Categories.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'add_product.html', context)
    elif request.method == 'POST':
        title = request.POST.get('title')  
        price = request.POST.get('price')  
        image = request.POST.get('image')  
        category = request.POST.get('prod_category')
        description = request.POST.get('description')  

        product = Product.objects.create(title=title, price=price, image=image, category_id=category, description=description)

        return redirect('product_card', pk=product.pk)

def product_view(request, pk):
    product = Product.objects.get(pk=pk)
    print(type(product.category))
    context = {
        'product': product
    }
    return render(request, 'detailed_view.html', context)

def product_delete(request, pk):
    Product.objects.filter(pk=pk).delete()
    return redirect('products')

def product_edit_view(request, pk):
    if request.method == 'GET':
        categories = Categories.objects.all()
        product = Product.objects.get(pk=pk)
        context = {
            'categories': categories,
            'product': product
        }
        return render(request, 'edit_product.html', context)
    elif request.method == 'POST':
        title = request.POST.get('title')  
        price = request.POST.get('price')  
        image = request.POST.get('image')  
        category = request.POST.get('prod_category')
        description = request.POST.get('description')  

        Product.objects.filter(pk=pk).update(title=title, price=price, image=image, category_id=category, description=description)

        return redirect('product_card', pk=pk)

def category_add_view(request):
    if request.method == 'GET':
        return render(request, 'add_category.html')
    elif request.method == 'POST':
        title = request.POST.get('title')  
        description = request.POST.get('description')  

        Categories.objects.create(title=title, description=description)
        return redirect('products')
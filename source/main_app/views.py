from django.shortcuts import render, redirect
from main_app.models import Product, Categories
from main_app.forms import ProductForm
# Create your views here.


def products_view(request):
    products = Product.objects.exclude(count=0).order_by('category', 'title')
    context = {
        'products': products
    }
    print(products)
    return render(request, 'main_page.html', context)

def product_add_view(request):
    if request.method == 'GET':
        categories = Categories.objects.all()
        form = ProductForm()
        context = {
            'categories': categories,
            'form': form
        }
        return render(request, 'add_product.html', context)
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = Product.objects.create(title=form.cleaned_data['title'], 
                                   price=form.cleaned_data['price'], 
                                   image=form.cleaned_data['image'], 
                                   category_id=form.cleaned_data['category'], 
                                   description=form.cleaned_data['description'])
            return redirect('product_card', pk=product.pk)
        else:
            return render(request, 'new_product', context={'form': form})

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
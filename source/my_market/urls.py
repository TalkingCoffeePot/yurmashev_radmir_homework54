"""
URL configuration for to_do_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main_app.views import ListProductsView, CreateProductView, CreateCategoryView, UpdateProduct, DetailProductView, DeleteProduct

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListProductsView.as_view(), name='products'),
    path('products/', ListProductsView.as_view(), name='products'),
    path('products/add', CreateProductView.as_view(), name='new_product'),
    path('categories/add/', CreateCategoryView.as_view(), name='new_category'),
    path('products/<int:product_pk>/', DetailProductView.as_view(), name='product_card'),
    path('products/<int:product_pk>/delete/', DeleteProduct.as_view(), name='prod_delete'),
    path('products/<int:product_pk>/edit/', UpdateProduct.as_view(), name='prod_edit')
]

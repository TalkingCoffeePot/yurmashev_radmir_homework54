from django.shortcuts import render, redirect
from main_app.models import Product, Categories
from main_app.forms import ProductForm, CategoriesForm
from main_app.forms import SimpleSearchForm
from urllib.parse import urlencode
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
# Create your views here.


class ListProductsView(ListView):
    template_name = 'main_page.html'
    context_object_name = 'products'
    model = Product
    paginate_by = 5
    paginate_orphans = 1
    
    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search'] = self.search_value
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(title__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

class DetailProductView(DeleteView):
    template_name = 'detailed_product.html'
    model = Product
    context_object_name = 'product'
    pk_url_kwarg = 'product_pk'

class CreateProductView(CreateView):
    template_name = 'add_product.html'
    form_class = ProductForm
    
    def get_success_url(self):
        return reverse('products')

class UpdateProduct(UpdateView):
    model = Product
    template_name = 'edit_product.html'
    pk_url_kwarg = 'product_pk'
    form_class = ProductForm
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('product_card', kwargs={'product_pk': self.object.pk})


class DeleteProduct(DeleteView):
    template_name = 'delete_product.html'
    pk_url_kwarg = 'product_pk'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('products')


class CreateCategoryView(CreateView):
    template_name = 'add_category.html'
    form_class = CategoriesForm
    
    def get_success_url(self):
        return reverse('products')
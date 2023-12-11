from django.contrib import admin
from main_app.models import Categories, Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'category', 'date', 'price', 'image', 'count']
    list_editable = ['title', 'description', 'category', 'price', 'image', 'count']

class CategoriesAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'description']
    list_editable=['title', 'description']


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Product, ProductAdmin)
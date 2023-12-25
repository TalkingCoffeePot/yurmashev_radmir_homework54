from django import forms
from django.forms import widgets
from main_app.models import Categories, Product
from main_app.validators import validate_zero
from django.core.exceptions import ValidationError

class CategoriesForm(forms.Form):
    class Meta:
        model = Categories
        fields = [
            'title',
            'description',
        ]


    def clean_title(self):
        value = self.cleaned_data.get('title')
        if Categories.objects.filter(title=value).exists():
            raise ValidationError(('Категория должна быть уникальной!'))
        return value


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'category',
            'price',
            'count',
            'image',
        ]

    def clean_summery(self):
        count = self.cleaned_data['count']
        if count < 0:
            raise forms.ValidationError("Слишком короткое название")
        return count

class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")

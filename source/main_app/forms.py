from django import forms
from django.forms import widgets
from main_app.models import Categories
from main_app.validators import validate_zero
from django.core.exceptions import ValidationError

class CategoriesForm(forms.Form):
    title = forms.CharField(label='Наименование', max_length=100, required=True)
    description = forms.CharField(label='Описание', max_length=1500, required=True, widget=widgets.Textarea)

    def clean_title(self):
        value = self.cleaned_data.get('title')
        if Categories.objects.filter(title=value).exists():
            raise ValidationError(('Категория должна быть уникальной!'))
        return value


class ProductForm(forms.Form):
    title = forms.CharField(label='Наименование', max_length=100, required=True)
    description = forms.CharField(label='Описание', max_length=1500, required=True, widget=widgets.Textarea)
    category = forms.ModelChoiceField(label='Категория', queryset=Categories.objects.all(), required=True)
    price = forms.DecimalField(label='Стоимость',max_digits=7, decimal_places=2, required=True)
    count = forms.IntegerField(label='Остаток', validators=[validate_zero], required=True)
    image = forms.CharField(label='Изображение', max_length=1000, required=True)

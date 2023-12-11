from django.db import models
from main_app.validators import validate_zero

# Create your models here.

class Categories(models.Model):
    title = models.CharField('Наименование', max_length=100, null=False, blank=False, unique=True)
    description = models.TextField('Описание', max_length=1500, null=True, blank=True)

    def __str__(self):
        return f'{self.pk}, {self.title}' 


class Product(models.Model):
    title = models.CharField('Наименование', max_length=100, null=False, blank=False)
    description = models.TextField('Описание', max_length=1500, null=True, blank=True)
    category = models.ForeignKey('main_app.Categories', on_delete=models.CASCADE, verbose_name='Категория', related_name='products', null=False, blank=False)
    date = models.DateTimeField('Дата создания', auto_now_add=True)
    price = models.DecimalField('Стоимость',max_digits=7, decimal_places=2, null=False, blank=False)
    count = models.IntegerField('Остаток', validators=[validate_zero], null=False, blank=False, default=0)
    image = models.CharField('Изображение', max_length=1000, null=False, blank=False)


    def __str__(self):
        return f'{self.pk}, {self.title}' 
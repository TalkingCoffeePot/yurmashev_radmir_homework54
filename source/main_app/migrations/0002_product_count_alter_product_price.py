# Generated by Django 4.2.7 on 2023-12-11 16:24

from django.db import migrations, models
import main_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count',
            field=models.IntegerField(default=0, validators=[main_app.validators.validate_zero], verbose_name='Остаток'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость'),
        ),
    ]

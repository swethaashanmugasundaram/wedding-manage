# Generated by Django 5.0.6 on 2024-06-12 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wesapp', '0009_carts_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carts',
            name='product_price',
        ),
    ]
# Generated by Django 5.0.6 on 2024-06-12 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wesapp', '0008_rename_cart_carts'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='product_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

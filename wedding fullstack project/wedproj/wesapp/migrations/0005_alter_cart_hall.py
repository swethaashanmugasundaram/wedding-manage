# Generated by Django 5.0.6 on 2024-06-12 12:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wesapp', '0004_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wesapp.traditional'),
        ),
    ]
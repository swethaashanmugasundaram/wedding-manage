# Generated by Django 5.0.6 on 2024-06-13 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wesapp', '0016_alter_order_created_at_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]

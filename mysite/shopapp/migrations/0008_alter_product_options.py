# Generated by Django 5.0 on 2024-04-15 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0007_order_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name', 'price']},
        ),
    ]

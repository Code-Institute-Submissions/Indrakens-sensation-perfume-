# Generated by Django 3.2.23 on 2024-03-29 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_rating',
        ),
    ]
# Generated by Django 3.2.23 on 2024-02-03 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_auto_20240203_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
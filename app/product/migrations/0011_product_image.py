# Generated by Django 4.2.6 on 2023-11-28 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_brand_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='products'),
        ),
    ]

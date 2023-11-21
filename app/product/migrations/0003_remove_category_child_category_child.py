# Generated by Django 4.2.6 on 2023-11-21 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_category_child'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='child',
        ),
        migrations.AddField(
            model_name='category',
            name='child',
            field=models.ManyToManyField(blank=True, null=True, to='product.category'),
        ),
    ]

# Generated by Django 2.1.3 on 2019-12-11 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_product', '0009_product_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='dimension',
            new_name='dimension_h',
        ),
        migrations.AddField(
            model_name='product',
            name='dimension_l',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='dimension_w',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
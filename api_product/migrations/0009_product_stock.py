# Generated by Django 2.1.3 on 2019-12-11 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_product', '0008_auto_20191125_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.CharField(blank=True, default='', max_length=800),
        ),
    ]

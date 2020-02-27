# Generated by Django 2.1.3 on 2019-02-18 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190212_0321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=400)),
                ('last_name', models.CharField(blank=True, default='', max_length=400)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('company', models.CharField(blank=True, default='', max_length=400)),
                ('phone', models.CharField(blank=True, default='', max_length=400)),
                ('apartment', models.CharField(blank=True, default='', max_length=400)),
                ('city', models.CharField(blank=True, default='', max_length=400)),
                ('country', models.CharField(blank=True, default='', max_length=400)),
                ('region', models.CharField(blank=True, default='', max_length=400)),
                ('postal_code', models.CharField(blank=True, default='', max_length=400)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]

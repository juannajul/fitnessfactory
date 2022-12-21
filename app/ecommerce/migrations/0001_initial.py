# Generated by Django 4.1.4 on 2022-12-12 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Category name')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Category slug')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=20, unique=True, verbose_name='Size')),
                ('size_type', models.CharField(blank=True, max_length=20, verbose_name='Size type')),
            ],
            options={
                'verbose_name': 'Sizes',
                'verbose_name_plural': 'Sizes',
            },
        ),
    ]

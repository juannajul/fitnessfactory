# Generated by Django 4.1.4 on 2023-01-03 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='size',
            options={'ordering': ['product'], 'verbose_name': 'Sizes', 'verbose_name_plural': 'Sizes'},
        ),
    ]

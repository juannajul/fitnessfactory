# Generated by Django 4.1.4 on 2022-12-29 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_alter_size_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Products'},
        ),
    ]
# Generated by Django 5.1.3 on 2024-11-23 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_collection_discount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='unit_price',
        ),
    ]

# Generated by Django 5.1.3 on 2024-12-18 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_orderitem_product_alter_product_collection_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
    ]

# Generated by Django 5.1.3 on 2024-11-23 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_slug_to_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='discount',
        ),
    ]

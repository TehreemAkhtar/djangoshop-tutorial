# Generated by Django 5.1.3 on 2024-12-31 05:35

import store.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_rename_image_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='store/images/', validators=[store.validators.validate_file_size]),
        ),
    ]

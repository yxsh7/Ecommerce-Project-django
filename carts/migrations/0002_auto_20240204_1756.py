# Generated by Django 3.1 on 2024-02-04 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='Quantity',
            new_name='quantity',
        ),
    ]

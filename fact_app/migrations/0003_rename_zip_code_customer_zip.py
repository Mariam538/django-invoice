# Generated by Django 4.1.7 on 2023-03-20 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fact_app', '0002_alter_customer_zip_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='zip_code',
            new_name='zip',
        ),
    ]

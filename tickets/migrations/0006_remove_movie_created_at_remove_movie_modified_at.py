# Generated by Django 4.2.8 on 2023-12-04 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_remove_customer_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='modified_at',
        ),
    ]
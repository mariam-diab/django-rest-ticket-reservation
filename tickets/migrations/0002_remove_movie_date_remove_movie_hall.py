# Generated by Django 4.2.7 on 2023-11-05 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='date',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='hall',
        ),
    ]

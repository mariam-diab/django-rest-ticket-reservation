# Generated by Django 4.2.7 on 2023-12-09 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0009_alter_movie_modified_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='modified_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

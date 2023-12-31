# Generated by Django 4.2.7 on 2023-11-03 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hall', models.CharField(max_length=5)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='tickets.customer')),
                ('movie_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='tickets.movie')),
            ],
        ),
    ]

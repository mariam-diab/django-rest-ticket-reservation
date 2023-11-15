from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Customer -- movie -- Reservation

class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)


class Movie(models.Model):
    name = models.CharField(max_length=50)
    hall = models.CharField(max_length=5)
    date = models.DateField()


class Reservation(models.Model):
    customer_name = models.ForeignKey(Customer, related_name="reservations", on_delete=models.CASCADE)
    movie_name = models.ForeignKey(Movie, related_name="reservations", on_delete=models.CASCADE)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)

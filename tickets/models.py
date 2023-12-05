from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Customer -- movie -- Reservation

class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Movie(models.Model):
    name = models.CharField(max_length=50)
    hall = models.CharField(max_length=5)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk is not None:  
            self.modified_at = timezone.now()
        super().save(*args, **kwargs)


class Reservation(models.Model):
    customer_name = models.ForeignKey(Customer, related_name="reservations", on_delete=models.CASCADE)
    movie_name = models.ForeignKey(Movie, related_name="reservations", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)

from django.contrib import admin
from .models import Movie, Customer, Reservation

# Register your models here.
admin.site.register(Movie)
admin.site.register(Customer)
admin.site.register(Reservation)
 
from django.contrib import admin

# Register your models here.
from restaurant.models import Menu,Booking
admin.site.register(Menu)
admin.site.register(Booking)
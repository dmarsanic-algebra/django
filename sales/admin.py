from django.contrib import admin
from .models import Customer, Offer, Invoice


admin.site.register(Customer)
admin.site.register(Offer)
admin.site.register(Invoice)

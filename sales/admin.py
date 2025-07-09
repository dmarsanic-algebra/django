from django.contrib import admin

from .models import Customer, Invoice, Offer


admin.site.register(Customer)
admin.site.register(Invoice)
admin.site.register(Offer)

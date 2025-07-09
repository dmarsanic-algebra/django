from django.contrib import admin

from .models import Ingredient, Product

admin.site.register(Ingredient)
admin.site.register(Product)

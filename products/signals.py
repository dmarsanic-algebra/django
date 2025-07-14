from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver
from .models import Product, Ingredient


# Flag to prevent recursive save
updating_product_price = False


@receiver(post_save, sender=Ingredient)
def update_product_total_price_on_ingredient_save(sender, instance, **kwargs):
    global updating_product_price
    # When an ingredient is saved, update all products that use this ingredient
    for product in instance.products.all():
        if not updating_product_price:
            updating_product_price = True
            product.calculate_total_price()
            product.save()
            updating_product_price = False


@receiver(post_delete, sender=Ingredient)
def update_product_total_price_on_ingredient_delete(sender, instance, **kwargs):
    global updating_product_price
    # When an ingredient is deleted, update all products that used this ingredient
    for product in instance.products.all():
        if not updating_product_price:
            updating_product_price = True
            product.calculate_total_price()
            product.save()
            updating_product_price = False


@receiver(post_delete, sender=Product)
def update_related_products_on_product_delete(sender, instance, **kwargs):
    global updating_product_price
    # When a product is deleted, update the total_price of all products that had this product as an ingredient
    for ingredient in instance.ingredients.all():
        for product in ingredient.products.all():
            if not updating_product_price:
                updating_product_price = True
                product.calculate_total_price()
                product.save()
                updating_product_price = False


@receiver(m2m_changed, sender=Product.ingredients.through)
def update_product_total_price_on_ingredient_change(sender, instance, action, **kwargs):
    global updating_product_price
    # When the ingredients of a product change, update the product's total price
    if action in ["post_add", "post_remove", "post_clear"]:
        if not updating_product_price:
            updating_product_price = True
            instance.calculate_total_price()
            instance.save()
            updating_product_price = False


@receiver(post_save, sender=Product)
def update_product_total_price_on_product_save(sender, instance, **kwargs):
    global updating_product_price
    # When a product is saved, update its total price
    if not updating_product_price:
        updating_product_price = True
        instance.calculate_total_price()
        instance.save()
        updating_product_price = False

from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver
from .models import Offer, Invoice


# Flag to prevent recursive save
updating_product_price = False


@receiver(post_delete, sender=Offer)
def update_related_products_on_product_delete(sender, instance, **kwargs):
    global updating_product_price
    # When a product is deleted, update the total_price of all products that had this product as an ingredient
    for ingredient in instance.products.all():
        for product in ingredient.ingredients.all():
            if not updating_product_price:
                updating_product_price = True
                product.calculate_total_price()
                product.save()
                updating_product_price = False


@receiver(m2m_changed, sender=Offer.products.through)
def update_product_total_price_on_ingredient_change(sender, instance, action, **kwargs):
    global updating_product_price
    # When the ingredients of a product change, update the product's total price
    if action in ["post_add", "post_remove", "post_clear"]:
        if not updating_product_price:
            updating_product_price = True
            instance.calculate_total_price()
            instance.save()
            updating_product_price = False


@receiver(post_save, sender=Offer)
def update_product_total_price_on_product_save(sender, instance, **kwargs):
    global updating_product_price
    # When a product is saved, update its total price
    if not updating_product_price:
        updating_product_price = True
        instance.calculate_total_price()
        instance.save()
        updating_product_price = False


@receiver(post_delete, sender=Invoice)
def update_related_products_on_product_delete(sender, instance, **kwargs):
    global updating_product_price
    # When a product is deleted, update the total_price of all products that had this product as an ingredient
    for product in instance.products.all():
        if not updating_product_price:
            updating_product_price = True
            product.calculate_total_price()
            product.save()
            updating_product_price = False


@receiver(m2m_changed, sender=Invoice.products.through)
def update_product_total_price_on_ingredient_change(sender, instance, action, **kwargs):
    global updating_product_price
    # When the ingredients of a product change, update the product's total price
    if action in ["post_add", "post_remove", "post_clear"]:
        if not updating_product_price:
            updating_product_price = True
            instance.calculate_total_price()
            instance.save()
            updating_product_price = False


@receiver(post_save, sender=Invoice)
def update_product_total_price_on_product_save(sender, instance, **kwargs):
    global updating_product_price
    # When a product is saved, update its total price
    if not updating_product_price:
        updating_product_price = True
        instance.calculate_total_price()
        instance.save()
        updating_product_price = False


@receiver(post_save, sender=Offer)
def calculate_total_price_post_save(sender, instance, created, **kwargs):
    if created:
        instance.calculate_total_price()
        instance.save()


@receiver(post_save, sender=Invoice)
def calculate_total_price_post_save(sender, instance, created, **kwargs):
    if created:
        instance.calculate_total_price()
        instance.save()

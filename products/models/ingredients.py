from django.db import models
from django.urls import reverse
from decimal import Decimal


class Ingredient(models.Model):
    name = models.CharField(
        max_length=150, help_text="Ingredient name", null=False, blank=False
    )
    code = models.CharField(
        max_length=20, help_text="Ingredient code", null=False, blank=False
    )
    description = models.CharField(
        max_length=150, help_text="Ingredient description", null=True, blank=True
    )
    base_price = models.DecimalField(
        max_digits=18,
        decimal_places=6,
        default=Decimal("0.00"),
        help_text="Ingredient price",
        null=True,
        blank=True,
    )
    price_mod = models.DecimalField(
        max_digits=5,
        decimal_places=3,
        default=Decimal("1.00"),
        help_text="Ingredient price modificator",
        null=True,
        blank=True,
    )
    total_price = models.DecimalField(
        max_digits=18,
        decimal_places=3,
        default=Decimal("1.00"),
        help_text="Ingredient total price",
        null=True,
        blank=True,
    )

    def __str__(self):
        if self.name != "" and self.code is not None:
            return f"{self.name} ({self.code})"
        else:
            return super().__str__()

    class Meta:
        ordering = ["name", "code"]

    def get_absolute_url(self):
        return reverse("ingredients-detail", kwargs={"pk": self.pk})

    def calculate_total_price(self):
        self.total_price = Decimal(self.base_price) * Decimal(self.price_mod)

    def save(self, *args, kwargs):
        self.calculate_total_price()
        super(Ingredient, self).save(*args, kwargs)

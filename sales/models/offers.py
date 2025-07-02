from django.db import models
from django.urls import reverse
from decimal import Decimal
from django.utils import timezone
from datetime import datetime

from account.models import User
from products.models import Product
from settings.models import Tenant
from ..models import Customer


class Offer(models.Model):
    STATUS_CHOICES = [
        ("sent", "Sent"),
        ("accepted", "Accepted"),
        ("canceled", "Canceled"),
        ("failed", "Failed"),
    ]

    offer_number = models.CharField(
        max_length=20, unique=True, blank=True, editable=False
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="sent")
    offer_note = models.TextField(max_length=1500, null=True, blank=True)
    date_created = models.DateTimeField(
        default=timezone.now, editable=True, null=True, blank=True
    )
    valid_to = models.DateTimeField(
        default=timezone.now, editable=True, null=True, blank=True
    )
    products = models.ManyToManyField(Product, related_name="offers", blank=True)
    total = models.DecimalField(
        max_digits=18,
        decimal_places=3,
        editable=False,
        default=Decimal("0.00"),
        null=True,
        blank=True,
    )
    total_sum = models.DecimalField(
        max_digits=18,
        decimal_places=3,
        editable=False,
        default=Decimal("0.00"),
        null=True,
        blank=True,
    )
    tax = models.DecimalField(
        max_digits=5, decimal_places=3, default=Decimal("0.00"), null=True, blank=True
    )
    total_tax = models.DecimalField(
        max_digits=5, decimal_places=3, default=Decimal("0.00"), null=True, blank=True
    )
    created_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="offers_created"
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.DO_NOTHING, related_name="offers"
    )
    tenant = models.ForeignKey(
        Tenant, on_delete=models.DO_NOTHING, related_name="offers"
    )

    def __str__(self):
        return f"Offer {self.offer_number}"

    class Meta:
        ordering = ["-date_created", "-offer_number"]

    def calculate_total_price(self):
        if len(self.products.all()) > 0:
            self.total = Decimal(
                sum(product.total_price for product in self.products.all())
            )
        else:
            self.total = Decimal(0.0)
        self.total_tax = self.total * Decimal(self.tax) / Decimal(100)
        self.total_sum = self.total + self.total_tax

    def save(self, *args, kwargs):
        if not self.offer_number:
            now = datetime.now()
            current_year_month = now.strftime("%Y%m")
            last_offer = (
                Offer.objects.filter(offer_number__startswith=f"0-{current_year_month}")
                .order_by("-offer_number")
                .first()
            )
            if last_offer:
                last_offer_number = int(last_offer.offer_number.split("-")[2])
            else:
                last_offer_number = 0
            self.offer_number = (
                f"0-{current_year_month}-{str(last_offer_number+1).zfill(3)}"
            )

            super(Offer, self).save(*args, kwargs)

    def get_absolute_url(self):
        return reverse("offers-detail", kwargs={"pk": self.pk})

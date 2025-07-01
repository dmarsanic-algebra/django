from django.db import models
from django.urls import reverse


class Tenant(models.Model):
    name = models.CharField(
        max_length=250, help_text="Tenant name", null=False, blank=False
    )
    vat_id = models.CharField(max_length=11, null=True, blank=True)
    street = models.CharField(max_length=250, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tenants-detail", kwargs={"pk": self.pk})

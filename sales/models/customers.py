from django.db import models
from django.urls import reverse
from settings.models import Gender, CustomerType


class Customer(models.Model):
    name = models.CharField(
        max_length=250, help_text="Customer name", null=False, blank=False
    )
    last_name = models.CharField(max_length=150, null=True, blank=True)
    vat_id = models.CharField(max_length=11, null=True, blank=True)
    street = models.CharField(max_length=250, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=150, null=True, blank=True)
    gender = models.ForeignKey(
        Gender, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    customer_type = models.ForeignKey(
        CustomerType, on_delete=models.DO_NOTHING, null=False, blank=False
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        if self.last_name != "" and self.last_name is not None:
            return f"{self.name} {self.last_name}"
        else:
            return self.name

    def get_absolute_url(self):
        return reverse("customers-detail", kwargs={"pk": self.pk})

from django.db import models
from django.urls import reverse


class Gender(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("genders-detail", kwargs={"pk": self.pk})

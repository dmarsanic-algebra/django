from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from ..models import CustomerType, Gender


class CustomerTypeListView(LoginRequiredMixin, ListView):
    model = CustomerType
    paginate_by = 10


class CustomerTypeDetailView(LoginRequiredMixin, DetailView):
    model = CustomerType


class CustomerTypeCreateView(LoginRequiredMixin, CreateView):
    model = CustomerType
    fields = ["name"]
    success_url = reverse_lazy("settings:customer-types")


class CustomerTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomerType
    fields = ["name"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("settings:customer-types")


class CustomerTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomerType
    success_url = reverse_lazy("settings:customer-types")

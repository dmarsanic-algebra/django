from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from ..models import CustomerType


class CustomerTypeListView(LoginRequiredMixin, ListView):
    model = CustomerType
    paginate_by = 10


class CustomerTypeDetailView(LoginRequiredMixin, DetailView):
    model = CustomerType


class CustomerTypeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = CustomerType
    fields = "__all__"  # ["name"]
    success_url = reverse_lazy("settings:customer-types")
    success_message = "CustomerType was created successfully!"


class CustomerTypeUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomerType
    fields = "__all__"  # ["name"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("settings:customer-types")
    success_message = "CustomerType was updated successfully!"


class CustomerTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomerType
    success_url = reverse_lazy("settings:customer-types")

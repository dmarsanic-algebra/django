from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Customer


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    paginate_by = 10


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    fields = "__all__"
    success_url = reverse_lazy("sales:customers")


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = "__all__"
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("sales:customers")


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy("sales:customers")

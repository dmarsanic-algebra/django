from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Invoice


class InvoiceListView(LoginRequiredMixin, ListView):
    model = Invoice
    paginate_by = 10


class InvoiceDetailView(LoginRequiredMixin, DetailView):
    model = Invoice


class InvoiceCreateView(LoginRequiredMixin, CreateView):
    model = Invoice
    fields = "__all__"
    success_url = reverse_lazy("sales:invoices")


class InvoiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Invoice
    fields = "__all__"
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("sales:invoices")


class InvoiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Invoice
    success_url = reverse_lazy("sales:invoices")

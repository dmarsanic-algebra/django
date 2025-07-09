from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Offer


class OfferListView(LoginRequiredMixin, ListView):
    model = Offer
    paginate_by = 10


class OfferDetailView(LoginRequiredMixin, DetailView):
    model = Offer


class OfferCreateView(LoginRequiredMixin, CreateView):
    model = Offer
    fields = "__all__"
    success_url = reverse_lazy("sales:offers")


class OfferUpdateView(LoginRequiredMixin, UpdateView):
    model = Offer
    fields = "__all__"
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("sales:offers")


class OfferDeleteView(LoginRequiredMixin, DeleteView):
    model = Offer
    success_url = reverse_lazy("sales:offers")

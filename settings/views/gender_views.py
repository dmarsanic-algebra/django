from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from ..models import Gender


class GenderListView(LoginRequiredMixin, ListView):
    model = Gender
    paginate_by = 10


class GenderDetailView(LoginRequiredMixin, DetailView):
    model = Gender


class GenderCreateView(LoginRequiredMixin, CreateView):
    model = Gender
    fields = ["name"]
    success_url = reverse_lazy("settings:genders")


class GenderUpdateView(LoginRequiredMixin, UpdateView):
    model = Gender
    fields = ["name"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("settings:genders")


class GenderDeleteView(LoginRequiredMixin, DeleteView):
    model = Gender
    success_url = reverse_lazy("settings:genders")

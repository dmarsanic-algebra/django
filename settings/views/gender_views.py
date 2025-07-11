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
from ..models import Gender


class GenderListView(LoginRequiredMixin, ListView):
    model = Gender
    paginate_by = 10


class GenderDetailView(LoginRequiredMixin, DetailView):
    model = Gender


class GenderCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Gender
    fields = "__all__"  # ["name"]
    success_url = reverse_lazy("settings:genders")
    success_message = "Gender was created successfully!"


class GenderUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Gender
    fields = "__all__"  # ["name"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("settings:genders")
    success_message = "Gender was updated successfully!"


class GenderDeleteView(LoginRequiredMixin, DeleteView):
    model = Gender
    success_url = reverse_lazy("settings:genders")

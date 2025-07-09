from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Ingredient


class IngredientListView(LoginRequiredMixin, ListView):
    model = Ingredient
    paginate_by = 10


class IngredientDetailView(LoginRequiredMixin, DetailView):
    model = Ingredient


class IngredientCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("products:ingredients")
    success_message = "Ingredient was created successfully!"

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.total_price = self.object.calculate_total_price
        self.object.save()
        return response


class IngredientUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Ingredient
    fields = "__all__"
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("products:ingredients")
    success_message = "Ingredient was updated successfully!"

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.total_price = self.object.calculate_total_price
        self.object.save()
        return response


class IngredientDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    success_url = reverse_lazy("products:ingredients")

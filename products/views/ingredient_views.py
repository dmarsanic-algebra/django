from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from ..models import Product


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 10


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = "__all__"
    success_url = reverse_lazy("products:products")

    def form_valid(self, form):
        # Save the form and get the new product object
        response = super().form_valid(form)
        self.object.total_price = self.object.calculate_total_price()
        self.object.save()
        return response


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = "__all__"
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("products:products")

    def form_valid(self, form):
        # Save the form and get the new product object
        response = super().form_valid(form)
        self.object.total_price = self.object.calculate_total_price()
        self.object.save()
        return response


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("products:products")

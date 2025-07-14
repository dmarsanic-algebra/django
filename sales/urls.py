from django.urls import path
from .views import (
    CustomerListView,
    CustomerDetailView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
    OfferListView,
    OfferDetailView,
    OfferCreateView,
    OfferUpdateView,
    OfferDeleteView,
    InvoiceListView,
    InvoiceDetailView,
    InvoiceCreateView,
    InvoiceUpdateView,
    InvoiceDeleteView,
)


urlpatterns = [
    path("customers/", CustomerListView.as_view(), name="customers"),
    path("customers/add/", CustomerCreateView.as_view(), name="customers-add"),
    path("customers/<int:pk>/", CustomerDetailView.as_view(), name="customers-detail"),
    path(
        "customers/<int:pk>/update/",
        CustomerUpdateView.as_view(),
        name="customers-update",
    ),
    path(
        "customers/<int:pk>/delete/",
        CustomerDeleteView.as_view(),
        name="customers-delete",
    ),
    path("offers/", OfferListView.as_view(), name="offers"),
    path("offers/add/", OfferCreateView.as_view(), name="offers-add"),
    path("offers/<int:pk>/", OfferDetailView.as_view(), name="offers-detail"),
    path("offers/<int:pk>/update/", OfferUpdateView.as_view(), name="offers-update"),
    path("offers/<int:pk>/delete/", OfferDeleteView.as_view(), name="offers-delete"),
    path("invoices/", InvoiceListView.as_view(), name="invoices"),
    path("invoices/add/", InvoiceCreateView.as_view(), name="invoices-add"),
    path("invoices/<int:pk>/", InvoiceDetailView.as_view(), name="invoices-detail"),
    path(
        "invoices/<int:pk>/update/", InvoiceUpdateView.as_view(), name="invoices-update"
    ),
    path(
        "invoices/<int:pk>/delete/", InvoiceDeleteView.as_view(), name="invoices-delete"
    ),
]

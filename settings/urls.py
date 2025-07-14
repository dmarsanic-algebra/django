from django.urls import path
from .views import (
    CustomerTypeListView,
    CustomerTypeDetailView,
    CustomerTypeCreateView,
    CustomerTypeDeleteView,
    CustomerTypeUpdateView,
    GenderListView,
    GenderDetailView,
    GenderUpdateView,
    GenderDeleteView,
    GenderCreateView,
    TenantListView,
    TenantDetailView,
    TenantUpdateView,
    SystemSettingsView,
)


urlpatterns = [
    path("system-settings/", SystemSettingsView.as_view(), name="system_settings"),
    path("customer-types/", CustomerTypeListView.as_view(), name="customer-types"),
    path(
        "customer-types/add/",
        CustomerTypeCreateView.as_view(),
        name="customer-types-add",
    ),
    path(
        "customer-types/<int:pk>/",
        CustomerTypeDetailView.as_view(),
        name="customer-types-detail",
    ),
    path(
        "customer-types/<int:pk>/update/",
        CustomerTypeUpdateView.as_view(),
        name="customer-types-update",
    ),
    path(
        "customer-types/<int:pk>/delete/",
        CustomerTypeDeleteView.as_view(),
        name="customer-types-delete",
    ),
    path("genders/", GenderListView.as_view(), name="genders"),
    path("genders/add/", GenderCreateView.as_view(), name="genders-add"),
    path("genders/<int:pk>/", GenderDetailView.as_view(), name="genders-detail"),
    path("genders/<int:pk>/update/", GenderUpdateView.as_view(), name="genders-update"),
    path("genders/<int:pk>/delete/", GenderDeleteView.as_view(), name="genders-delete"),
    path("tenants/", TenantListView.as_view(), name="tenants"),
    path("tenants/<int:pk>/", TenantDetailView.as_view(), name="tenants-detail"),
    path("tenants/<int:pk>/update/", TenantUpdateView.as_view(), name="tenants-update"),
]

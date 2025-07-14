from django.urls import path
from .views import (
    ProductCreateView,
    ProductListView,
    ProductDeleteView,
    ProductDetailView,
    ProductUpdateView,
    IngredientCreateView,
    IngredientDeleteView,
    IngredientDetailView,
    IngredientListView,
    IngredientUpdateView,
)


urlpatterns = [
    path("products/", ProductListView.as_view(), name="products"),
    path("products/add/", ProductCreateView.as_view(), name="products-add"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="products-detail"),
    path(
        "products/<int:pk>/update/", ProductUpdateView.as_view(), name="products-update"
    ),
    path(
        "products/<int:pk>/delete/", ProductDeleteView.as_view(), name="products-delete"
    ),
    path("ingredients/", IngredientListView.as_view(), name="ingredients"),
    path("ingredients/add/", IngredientCreateView.as_view(), name="ingredients-add"),
    path(
        "ingredients/<int:pk>/",
        IngredientDetailView.as_view(),
        name="ingredients-detail",
    ),
    path(
        "ingredients/<int:pk>/update/",
        IngredientUpdateView.as_view(),
        name="ingredients-update",
    ),
    path(
        "ingredients/<int:pk>/delete/",
        IngredientDeleteView.as_view(),
        name="ingredients-delete",
    ),
]

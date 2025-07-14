from django.urls import path
from .views import HomePageView, AboutUsPageView, ContactUsPageView, DashboardPageView

urlpatterns = [
    path("about/", AboutUsPageView.as_view(), name="about"),
    path("contact-us/", ContactUsPageView.as_view(), name="contact_us"),
    path("dashboard/", DashboardPageView.as_view(), name="dashboard"),
    path("", HomePageView.as_view(), name="index"),
]

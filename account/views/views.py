from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from ..models import User

username_validator = UnicodeUsernameValidator()


class UserListView(LoginRequiredMixin, ListView):
    model = User
    paginate_by = 10
    template_name = "registration/user_list.html"


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(
        required=True, help_text="Email adress.", widget=(forms.TextInput())
    )
    first_name = forms.CharField(
        required=True, help_text="Frist Name", widget=(forms.TextInput())
    )
    last_name = forms.CharField(
        required=True, help_text="Last Name", widget=(forms.TextInput())
    )
    password1 = forms.CharField(label=_("Password"), widget=(forms.PasswordInput()))
    password2 = forms.CharField(
        label=_("Password Confirmation"), widget=(forms.PasswordInput())
    )

    class Meta:
        model = User
        fields = (
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "description",
            "job_position",
            "is_activate",
            "is_staff",
            "is_superuser",
        )


class UserCreateView(LoginRequiredMixin, CreateView):
    form_class = UserCreateForm
    template_name = "registration/user_form.html"
    success_url = reverse_lazy("account:users")


class UserUpdateForm(UserChangeForm):
    email = forms.EmailField(
        required=True, help_text="Email adress.", widget=(forms.TextInput())
    )
    first_name = forms.CharField(
        required=True, help_text="Frist Name", widget=(forms.TextInput())
    )
    last_name = forms.CharField(
        required=True, help_text="Last Name", widget=(forms.TextInput())
    )
    new_password = forms.CharField(
        label=_("New Password"), widget=(forms.PasswordInput()), required=False
    )

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "description",
            "job_position",
            "is_activate",
            "is_staff",
            "is_superuser",
            "new_password",
        )


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "registration/user_update_form.html"
    success_url = reverse_lazy("account:users")

    def form_valid(self, form):
        response = super().form_valid(form)
        new_password = form.cleaned_data.get("new_password")
        if new_password:
            self.object.set_password(new_password)
            self.object.save()
            messages.success(
                self.request,
                f"Password for user {self.object.first_name} has been changed successfully.",
            )
        else:
            messages.success(
                self.request,
                f"User {self.object.first_name} has been updated successfully.",
            )
        return response


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "registration/user_confirm_delete.html"
    seuccess_url = reverse_lazy("account:users")


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("pages:index")

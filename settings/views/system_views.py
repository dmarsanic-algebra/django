from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from account.models import User
from sales.models import Customer, Invoice, Offer
from products.models import Ingredient, Product
from ..models import Gender, CustomerType, Tenant
from decimal import Decimal


from faker import Faker


class SystemSettingsView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = "system_settings.html"

    def post(self, request, *args, **kwargs):

        action = request.POST.get("action")

        if action == "seed":
            self.seed_database()
            messages.success(request, "Baza podataka je uspjesno inicijalizirana")
        elif action == "clean":
            messages.warning(request, "Brisanje baze podataka nije omoguceno.")
            # self.clean_database()

        return redirect("settigns:system-settings")

    def clean_database(self):
        for model in [
            Gender,
            CustomerType,
            Tenant,
            Ingredient,
            Product,
            Customer,
            Invoice,
            Offer,
            User,
        ]:
            model.objects.all().delete()

    def seed_database(self):
        faker = Faker()

        if not User.objects.filter(email="admin@algebra.pydev").exists():
            User.objects.create_superuser(
                email="admin@algebra.pydev",
                password="admin",
                first_name="Admin",
                last_name="User",
            )
            messages.success(self.request, "Superkorisnik je kreiran.")

        for i in range(3):
            email = f"user{i}@gmail.com"
            if not User.objects.filter(email=email).exists():
                User.objects.create_user(
                    email=email, password=f"{i}{i}{i}{i}{i}{i}{i}{i}"
                )
                messages.success(self.request, f"Korisnik {email} je kreiran.")

        if not Tenant.objects.exists():
            Tenant.objects.create(name="Neki Tenant")
            messages.success(self.request, "Tenant kreiran.")

        genders = ["Male", "Female", "Non-binary", "Prefer not to say"]
        for gender in genders:
            Gender.objects.get_or_create(name=gender)
        messages.success(self.request, "Spolovi su kreirani.")

        types = ["Company", "Person"]
        for type in types:
            CustomerType.objects.get_or_create(name=type)
        messages.success(self.request, "Tipovi kupaca su kreirani.")

        ingredients = ["Salt", "Sugar", "Flour"]
        for ingredient in ingredients:
            Ingredient.objects.get_or_create(
                name=ingredient, code=ingredient[:3].upper()
            )
        messages.success(self.request, "Sastojci su kreirani.")

        products = ["Bread", "Milk", "Juice"]
        for product in products:
            Product.objects.get_or_create(name=product, code=product[:3].upper())
        messages.success(self.request, "Proizvodi su kreirani.")

        for i in range(5):
            first_name = faker.first_name()
            last_name = faker.last_name()

            gender = Gender.objects.order_by("?").first()
            customer_type = CustomerType.objects.order_by("?").first()

            Customer.objects.get_or_create(
                name=first_name,
                last_name=last_name,
                vat_id=faker.unique.msisdn()[0:11],
                street=faker.street_address(),
                postal_code=faker.postcode(),
                city=faker.city(),
                country=faker.country(),
                gender=gender,
                customer_type=customer_type,
            )
        messages.success(self.request, "Kupci su kreirani.")

        for i in range(5):
            customer = Customer.objects.order_by("?").first()
            created_by = User.objects.filter(is_superuser=True).first()
            tenant = Tenant.objects.first()

            offer = Offer.objects.create(
                created_by=created_by,
                customer=customer,
                tenant=tenant,
                date_created=faker.date_this_year(),
                valid_to=faker.future_datetime(),
                tax=Decimal("25.0"),
            )

            products = list(Product.objects.order_by("?")[:3])
            offer.products.set(products)

            offer.calculate_total_price()
            offer.save()
        messages.success(self.request, "Ponude su kreirane.")

        for i in range(3):
            customer = Customer.objects.order_by("?").first()
            created_by = User.objects.filter(is_superuser=True).first()
            tenant = Tenant.objects.first()
            offer = Offer.objects.order_by("?").first()

            invoice = Invoice.objects.create(
                created_by=created_by,
                customer=customer,
                tenant=tenant,
                offer=offer,
                date_created=faker.date_this_year(),
                valid_to=faker.future_datetime(),
                tax=Decimal("25.0"),
            )

            products = list(Product.objects.order_by("?")[:3])
            invoice.products.set(products)

            invoice.calculate_total_price()
            invoice.save()
        messages.success(self.request, "Racuni kreirani")

import random
from datetime import datetime, timedelta
from decimal import Decimal

from django.utils import timezone
from django.db import transaction

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model

from products.models import Ingredient, Product
from sales.models import Customer, Offer, Invoice
from settings.models import Gender, CustomerType, Tenant

from faker import Faker


class SystemSettingsView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = "settings/system_settings.html"
    success_message = ""

    def post(self, request, *args, **kwargs):
        action = request.POST.get("action")

        if action == "seed":
            self.seed_database(request)
        elif action == "clean":
            pass
            # self.clean_database()
            messages.add_message(request, messages.INFO, "Database can't be cleand!")

        return redirect(reverse("settings:system_settings"))

    def clean_database(self):
        models = [Gender, CustomerType, Ingredient, Product, Customer, Offer, Invoice]

        # Delete all data from each model
        for model in models:
            model.objects.all().delete()

    def seed_database(self, request):
        # Create Users
        User = get_user_model()

        if not User.objects.filter(email="admin@algebra.pydev").exists():
            User.objects.create_superuser(
                email="admin@algebra.pydev",
                first_name="Super",
                last_name="Administrator",
                password="Pa$$w0rd!",
            )
            messages.add_message(
                request,
                messages.SUCCESS,
                "Superuser is successfully added to the database.",
            )

            # Job positions
        job_positions = ["Employee", "Manager", "CEO"]
        user_data = [
            ("ivan.horvat@algebra.pydev", "Ivan", "Horvat", job_positions[0]),
            ("ana.kovacevic@algebra.pydev", "Ana", "Kovačević", job_positions[0]),
            ("marko.maric@algebra.pydev", "Marko", "Marić", job_positions[0]),
            ("ivana.babic@algebra.pydev", "Ivana", "Babić", job_positions[0]),
            ("petar.juric@algebra.pydev", "Petar", "Jurić", job_positions[0]),
            ("marija.novak@algebra.pydev", "Marija", "Novak", job_positions[0]),
            ("tomislav.raic@algebra.pydev", "Tomislav", "Raić", job_positions[0]),
            ("lucija.peric@algebra.pydev", "Lucija", "Perić", job_positions[1]),
            ("ante.bosnjak@algebra.pydev", "Ante", "Bošnjak", job_positions[1]),
            ("maja.tomic@algebra.pydev", "Maja", "Tomić", job_positions[2]),
        ]

        for email, first_name, last_name, job_position in user_data:
            if not User.objects.filter(email=email).exists():
                User.objects.create_user(
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    job_position=job_position,
                    password="Pa$$w0rd!",
                    is_staff=True,
                    is_active=True,
                )
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Users are successfully added to the database.",
                )

        messages.add_message(
            request, messages.INFO, "Users already exist in the database."
        )

        # Create Tenants
        tenant = [
            "Mala firma j.d.o.o.",
            "12345678987",
            "Ilica 1",
            "10000",
            "Zagreb",
            "Hrvatska",
        ]
        if not Tenant.objects.exists():
            Tenant.objects.create(
                name=tenant[0],
                vat_id=tenant[1],
                street=tenant[2],
                postal_code=tenant[3],
                city=tenant[4],
                country=tenant[5],
            )
            messages.add_message(
                request,
                messages.SUCCESS,
                "Tenant is successfully added to the database.",
            )
        else:
            messages.add_message(
                request, messages.INFO, "Tenant already exist in the database."
            )

        # Create Genders
        genders = ["Male", "Female", "Non-binary", "Prefer not to say"]
        if not Gender.objects.exists():
            for gender in genders:
                Gender.objects.create(name=gender)
            messages.add_message(
                request,
                messages.SUCCESS,
                "Genders are successfully added to the database.",
            )
        else:
            messages.add_message(
                request, messages.INFO, "Genders already exist in the database."
            )

        # Create Customer Types
        customer_types = ["Company", "Person"]
        if not CustomerType.objects.exists():
            for ct in customer_types:
                CustomerType.objects.create(name=ct)
            messages.add_message(
                request,
                messages.SUCCESS,
                "Customer Types are successfully added to the database.",
            )
        else:
            messages.add_message(
                request, messages.INFO, "Customer Types already exist in the database."
            )

        # Create Ingredients
        ingredients = [
            ("Plastic Resin", "PLR-001", "High-density polyethylene", 2.50, 1.02, 2.55),
            (
                "Aluminum Sheet",
                "ALS-002",
                "2mm thickness aluminum sheet",
                3.75,
                1.05,
                3.94,
            ),
            ("Stainless Steel Screws", "SSS-003", "M3 x 10mm screws", 0.10, 1.01, 0.10),
            ("Lithium Battery", "LBT-004", "3.7V 1000mAh battery", 4.00, 1.08, 4.32),
            ("Copper Wire", "CWR-005", "1mm diameter copper wire", 0.20, 1.03, 0.21),
            ("LED Display", "LED-006", "16x2 character LCD display", 2.00, 1.10, 2.20),
            (
                "Microcontroller",
                "MCU-007",
                "ATmega328P microcontroller",
                5.00,
                1.07,
                5.35,
            ),
            ("GPS Module", "GPS-008", "U-blox NEO-6M GPS module", 12.00, 1.15, 13.80),
            ("PCB Board", "PCB-009", "Double-sided PCB board", 1.50, 1.02, 1.53),
            (
                "Soldering Wire",
                "SOW-010",
                "0.8mm lead-free solder wire",
                0.05,
                1.01,
                0.05,
            ),
            (
                "Heat Shrink Tubing",
                "HST-011",
                "2:1 ratio heat shrink tubing",
                0.10,
                1.02,
                0.10,
            ),
            (
                "Ferrite Bead",
                "FBD-012",
                "EMI suppression ferrite bead",
                0.02,
                1.01,
                0.02,
            ),
            (
                "Ceramic Capacitor",
                "CCA-013",
                "100nF ceramic capacitor",
                0.01,
                1.00,
                0.01,
            ),
            ("Resistor", "RES-014", "10k ohm resistor", 0.01, 1.00, 0.01),
            (
                "Voltage Regulator",
                "VRG-015",
                "LM7805 voltage regulator",
                0.50,
                1.04,
                0.52,
            ),
            ("Diode", "DIO-016", "1N4007 rectifier diode", 0.02, 1.00, 0.02),
            (
                "Thermal Paste",
                "THP-017",
                "High-performance thermal paste",
                1.00,
                1.05,
                1.05,
            ),
            ("Enclosure", "ENC-018", "ABS plastic enclosure", 3.00, 1.10, 3.30),
            ("Ribbon Cable", "RBC-019", "10-wire ribbon cable", 0.50, 1.02, 0.51),
            ("Push Button", "PBM-020", "Momentary push button", 0.15, 1.02, 0.15),
            ("Transistor", "TRN-021", "NPN transistor", 0.02, 1.00, 0.02),
            ("Connector", "CON-022", "2-pin JST connector", 0.10, 1.02, 0.10),
            ("Heat Sink", "HSK-023", "Aluminum heat sink", 0.25, 1.03, 0.26),
            (
                "Crystal Oscillator",
                "CRO-024",
                "16MHz crystal oscillator",
                0.05,
                1.02,
                0.05,
            ),
            ("Relay", "RLY-025", "5V relay module", 1.00, 1.05, 1.05),
            ("Potentiometer", "POT-026", "10k ohm potentiometer", 0.20, 1.02, 0.20),
            ("Tactile Switch", "TSW-027", "6mm tactile switch", 0.02, 1.01, 0.02),
            ("Inductor", "IND-028", "10uH inductor", 0.03, 1.01, 0.03),
            ("MOSFET", "MOS-029", "N-channel MOSFET", 0.50, 1.04, 0.52),
            (
                "Ethernet Module",
                "ETH-030",
                "ENC28J60 Ethernet module",
                7.00,
                1.10,
                7.70,
            ),
            ("Thermistor", "THM-031", "10k ohm thermistor", 0.10, 1.01, 0.10),
            ("Optocoupler", "OPC-032", "4N35 optocoupler", 0.20, 1.02, 0.20),
            ("Piezo Buzzer", "PBZ-033", "5V piezo buzzer", 0.50, 1.03, 0.52),
            ("DC Motor", "DCM-034", "6V DC motor", 3.00, 1.10, 3.30),
            ("Motor Driver", "MDR-035", "L298N motor driver", 4.00, 1.08, 4.32),
            ("Light Sensor", "LSR-036", "Photodiode light sensor", 0.30, 1.02, 0.31),
            ("Speaker", "SPK-037", "8 ohm speaker", 2.00, 1.05, 2.10),
            (
                "Temperature Sensor",
                "TMP-038",
                "DS18B20 temperature sensor",
                1.50,
                1.05,
                1.58,
            ),
            ("Humidity Sensor", "HMS-039", "DHT22 humidity sensor", 3.00, 1.10, 3.30),
            ("Pressure Sensor", "PRS-040", "BMP280 pressure sensor", 4.00, 1.08, 4.32),
            ("Proximity Sensor", "PRX-041", "IR proximity sensor", 1.00, 1.05, 1.05),
            ("Gyroscope", "GYR-042", "MPU6050 gyroscope module", 3.50, 1.10, 3.85),
            ("Accelerometer", "ACC-043", "ADXL345 accelerometer", 2.50, 1.08, 2.70),
            (
                "Ultrasonic Sensor",
                "ULS-044",
                "HC-SR04 ultrasonic sensor",
                2.00,
                1.07,
                2.14,
            ),
            (
                "Hall Effect Sensor",
                "HLS-045",
                "A3144 Hall effect sensor",
                0.50,
                1.03,
                0.52,
            ),
            ("Vibration Motor", "VBM-046", "3V vibration motor", 1.50, 1.05, 1.58),
            ("Light Emitting Diode", "LED-047", "5mm red LED", 0.02, 1.01, 0.02),
            (
                "Capacitive Touch Sensor",
                "CTS-048",
                "TTP223 touch sensor",
                1.00,
                1.05,
                1.05,
            ),
            ("RFID Module", "RFID-049", "RC522 RFID module", 5.00, 1.07, 5.35),
            ("OLED Display", "OLE-050", "0.96 inch OLED display", 6.00, 1.10, 6.60),
        ]
        if not Ingredient.objects.exists():
            for (
                name,
                code,
                description,
                base_price,
                price_mod,
                total_price,
            ) in ingredients:
                Ingredient.objects.create(
                    name=name,
                    code=code,
                    description=description,
                    base_price=Decimal(base_price),
                    price_mod=Decimal(price_mod),
                    total_price=Decimal(total_price),
                )
            messages.add_message(
                request,
                messages.SUCCESS,
                "Ingredients are successfully added to the database.",
            )
        else:
            ingredient_objects = []
            messages.add_message(
                request, messages.INFO, "Ingredients already exist in the database."
            )

        # Create Products
        products = [
            (
                "GPS Tracker for Pets",
                "PROD-001",
                "Compact GPS tracker for pets",
                1.125,
                50.43,
                [33, 37, 45],
            ),
            (
                "Hiker Safety Device",
                "PROD-002",
                "Safety device with GPS for hikers",
                1.015,
                50.43,
                [2, 23, 17],
            ),
            (
                "Vehicle Tracking System",
                "PROD-003",
                "System for tracking vehicles",
                1.121,
                50.43,
                [33, 41, 5, 42, 31],
            ),
            (
                "Worker Locator",
                "PROD-004",
                "Locator for infrastructure workers",
                1.014,
                50.43,
                [9, 30, 41, 23, 47, 32, 22, 20],
            ),
            (
                "Child Safety Tracker",
                "PROD-005",
                "GPS tracker for child safety",
                1.128,
                50.43,
                [37, 15, 45, 47, 32, 42, 8],
            ),
            (
                "Senior Citizen Tracker",
                "PROD-006",
                "Tracker for senior citizens",
                1.141,
                50.43,
                [46, 32],
            ),
            (
                "Asset Tracker",
                "PROD-007",
                "Tracker for valuable assets",
                1.034,
                50.43,
                [5, 44, 45, 2, 48, 8, 14],
            ),
            (
                "Pet Collar Tracker",
                "PROD-008",
                "GPS tracker collar for pets",
                1.008,
                50.43,
                [36, 28, 1, 3, 2],
            ),
            (
                "Outdoor Activity Tracker",
                "PROD-009",
                "Tracker for outdoor activities",
                1.06,
                50.43,
                [2, 15, 19, 5, 3],
            ),
            (
                "Bike GPS Tracker",
                "PROD-010",
                "GPS tracker for bicycles",
                1.06,
                50.43,
                [18, 17, 46, 48, 41, 22, 37, 49, 45],
            ),
            (
                "Personal Locator",
                "PROD-011",
                "Personal GPS locator",
                1.014,
                50.43,
                [16, 18, 4, 20],
            ),
            (
                "Luggage Tracker",
                "PROD-012",
                "GPS tracker for luggage",
                1.076,
                50.43,
                [50, 7],
            ),
            (
                "Employee Tracker",
                "PROD-013",
                "GPS tracker for employees",
                1.121,
                50.43,
                [16, 37, 14, 7, 26],
            ),
            (
                "Tool Tracker",
                "PROD-014",
                "GPS tracker for tools",
                1.058,
                50.43,
                [41, 18, 11, 38, 26, 30, 40, 28, 33],
            ),
            (
                "Drone GPS Module",
                "PROD-015",
                "GPS module for drones",
                1.071,
                50.43,
                [23, 27, 40, 47, 9, 13, 6, 16],
            ),
            (
                "Vehicle GPS Tracker",
                "PROD-016",
                "GPS tracker for vehicles",
                1.023,
                50.43,
                [27, 15, 48, 3],
            ),
            (
                "Boat GPS Tracker",
                "PROD-017",
                "GPS tracker for boats",
                1.091,
                50.43,
                [32, 28, 46, 14, 3],
            ),
            (
                "Motorcycle GPS Tracker",
                "PROD-018",
                "GPS tracker for motorcycles",
                1.049,
                50.43,
                [25, 35, 39, 7],
            ),
            (
                "Portable GPS Tracker",
                "PROD-019",
                "Portable GPS tracker",
                1.098,
                50.43,
                [33, 25, 3, 45, 35],
            ),
            (
                "Adventure Tracker",
                "PROD-020",
                "GPS tracker for adventurers",
                1.012,
                50.43,
                [47, 19, 16, 35, 44, 34],
            ),
        ]
        if not Product.objects.exists():
            try:
                with transaction.atomic():
                    for (
                        name,
                        code,
                        description,
                        price_mod,
                        fixed_costs,
                        product_ingredients_ids,
                    ) in products:
                        ingredients_from_db = Ingredient.objects.filter(
                            pk__in=product_ingredients_ids
                        )
                        product = Product.objects.create(
                            name=name,
                            code=code,
                            description=description,
                            price_mod=Decimal(price_mod),
                            fixed_costs=Decimal(fixed_costs),
                        )
                        product.ingredients.set(ingredients_from_db)

                        product.save()
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        "Products are successfully added to the database.",
                    )
            except Exception as e:
                messages.add_message(
                    request, messages.ERROR, f"An error occurred: {str(e)}"
                )
        else:
            messages.add_message(
                request, messages.INFO, "Products already exist in the database."
            )

        # Create Customers
        customers = [
            (
                "Mia",
                "Meyer",
                "76182455402",
                "Ulmenstraße 40",
                "75467",
                "Zurich",
                "Swiss",
                "Female",
                "Person",
            ),
            (
                "Lukas",
                "Huber",
                "85341249818",
                "Ulmenstraße 91",
                "12419",
                "Vienna",
                "Austria",
                "Male",
                "Person",
            ),
            (
                "Nina",
                "Novak",
                "90038191869",
                "Glavna ulica 60",
                "48142",
                "Ljubljana",
                "Slovenia",
                "Male",
                "Person",
            ),
            (
                "Julia",
                "Müller",
                "16149294401",
                "Parkstraße 10",
                "94072",
                "Berlin",
                "Germany",
                "Female",
                "Person",
            ),
            (
                "Laura",
                "Schneider",
                "40986216739",
                "Eichenstraße 63",
                "72558",
                "Berlin",
                "Germany",
                "Prefer not to say",
                "Person",
            ),
            (
                "Ivan",
                "Horvat",
                "93571648200",
                "Brijestova ulica 87",
                "37158",
                "Zagreb",
                "Croatia",
                "Male",
                "Person",
            ),
            (
                "Leo",
                "Fischer",
                "19024830299",
                "Kiefernstraße 2",
                "84926",
                "Zurich",
                "Swiss",
                "Male",
                "Person",
            ),
            (
                "Paul",
                "Schmidt",
                "12837048294",
                "Hauptstraße 53",
                "72084",
                "Graz",
                "Austria",
                "Male",
                "Person",
            ),
            (
                "Ana",
                "Kovač",
                "83720498273",
                "Hrastova ulica 5",
                "21930",
                "Split",
                "Croatia",
                "Female",
                "Person",
            ),
            (
                "Lara",
                "Meier",
                "30481294837",
                "Höhenstraße 32",
                "73284",
                "Munich",
                "Germany",
                "Non-binary",
                "Person",
            ),
            (
                "Suncokret d.o.o.",
                "",
                "38457298372",
                "Glavna ulica 15",
                "34293",
                "Zagreb",
                "Croatia",
                None,
                "Company",
            ),
            (
                "Zelena Dolina d.o.o.",
                "",
                "20485739485",
                "Visoka ulica 20",
                "23948",
                "Ljubljana",
                "Slovenia",
                None,
                "Company",
            ),
            (
                "Kraftwerk AG",
                "",
                "58394038475",
                "Höhenstraße 55",
                "72934",
                "Vienna",
                "Austria",
                None,
                "Company",
            ),
            (
                "Sternenlicht GmbH",
                "",
                "59384758394",
                "Eichenstraße 10",
                "58293",
                "Zurich",
                "Swiss",
                None,
                "Company",
            ),
            (
                "Glanz & Partner GmbH",
                "",
                "95837492034",
                "Kiefernstraße 8",
                "12384",
                "Berlin",
                "Germany",
                None,
                "Company",
            ),
            (
                "Zlatna Polja d.o.o.",
                "",
                "58293084758",
                "Park ulica 6",
                "83920",
                "Split",
                "Croatia",
                None,
                "Company",
            ),
            (
                "Sončni Vrtovi d.o.o.",
                "",
                "10394857329",
                "Glavna ulica 2",
                "23094",
                "Maribor",
                "Slovenia",
                None,
                "Company",
            ),
            (
                "Silberhafen GmbH",
                "",
                "29485739485",
                "Hauptstraße 1",
                "58293",
                "Linz",
                "Austria",
                None,
                "Company",
            ),
            (
                "Himmelsfluss GmbH",
                "",
                "39485793847",
                "Ulmenstraße 25",
                "37492",
                "Geneva",
                "Swiss",
                None,
                "Company",
            ),
            (
                "Südlicht GmbH",
                "",
                "58394028394",
                "Parkstraße 9",
                "83792",
                "Munich",
                "Germany",
                None,
                "Company",
            ),
            (
                "Vesela Tvornica d.o.o.",
                "",
                "93847583947",
                "Brijestova ulica 19",
                "32948",
                "Osijek",
                "Croatia",
                None,
                "Company",
            ),
            (
                "Vesela Trgovina d.o.o.",
                "",
                "49857394857",
                "Visoka ulica 45",
                "23948",
                "Celje",
                "Slovenia",
                None,
                "Company",
            ),
            (
                "Morgenstern GmbH",
                "",
                "29485739485",
                "Eichenstraße 22",
                "23498",
                "Graz",
                "Austria",
                None,
                "Company",
            ),
            (
                "Goldene Wege AG",
                "",
                "59384758394",
                "Ulmenstraße 33",
                "32849",
                "Basel",
                "Swiss",
                None,
                "Company",
            ),
            (
                "Nordwind GmbH",
                "",
                "10394857394",
                "Parkstraße 20",
                "49283",
                "Hamburg",
                "Germany",
                None,
                "Company",
            ),
            (
                "Plavi Val d.o.o.",
                "",
                "58394038594",
                "Hrastova ulica 17",
                "92384",
                "Rijeka",
                "Croatia",
                None,
                "Company",
            ),
            (
                "Modri Valovi d.o.o.",
                "",
                "20394857392",
                "Glavna ulica 11",
                "32948",
                "Koper",
                "Slovenia",
                None,
                "Company",
            ),
            (
                "Blütenfeld GmbH",
                "",
                "29384759384",
                "Hauptstraße 30",
                "38475",
                "Bern",
                "Swiss",
                None,
                "Company",
            ),
        ]

        if not Customer.objects.exists():
            try:
                with transaction.atomic():
                    for (
                        name,
                        last_name,
                        vat_id,
                        street,
                        postal_code,
                        city,
                        country,
                        gender_name,
                        customer_type_name,
                    ) in customers:
                        gender = (
                            Gender.objects.filter(name=gender_name).first()
                            if gender_name
                            else None
                        )
                        customer_type = CustomerType.objects.filter(
                            name=customer_type_name
                        ).first()

                        if customer_type_name == "Company":
                            Customer.objects.create(
                                name=name,
                                vat_id=vat_id,
                                street=street,
                                postal_code=postal_code,
                                city=city,
                                country=country,
                                customer_type=customer_type,
                            )
                        else:
                            Customer.objects.create(
                                name=name,
                                last_name=last_name,
                                vat_id=vat_id,
                                street=street,
                                postal_code=postal_code,
                                city=city,
                                country=country,
                                gender=gender,
                                customer_type=customer_type,
                            )

                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        "Customers are successfully added to the database.",
                    )
            except Exception as e:
                messages.add_message(
                    request, messages.ERROR, f"An error occurred: {str(e)}"
                )
        else:
            messages.add_message(
                request, messages.INFO, "Customers already exist in the database."
            )

        # Create Offers and Invoices
        users_from_db = list(User.objects.all())
        tenant_from_db = list(Tenant.objects.all())
        customers_from_db = list(Customer.objects.all())
        product_from_db = list(Product.objects.all())
        fake = Faker()

        if not Offer.objects.exists():
            for i in range(25):
                offer_statues = [
                    ("sent", "Sent"),
                    ("accepted", "Accepted"),
                    ("canceled", "Canceled"),
                    ("failed", "Failed"),
                ]

                date_created = fake.date_time_between(start_date="-5y", end_date="now")
                offer_number = f"O-{date_created.year}{date_created.month:02d}-{str(i + 1).zfill(3)}"

                valid_to_values = [0, 10, 15, 30, 45, 60]
                valid_to = date_created + timedelta(days=random.choice(valid_to_values))
                offer = Offer.objects.create(
                    offer_number=offer_number,
                    status=random.choice(offer_statues)[0],
                    offer_note=f"Offer note for {offer_number}",
                    date_created=date_created,
                    valid_to=valid_to,
                    tax=Decimal(25.00),
                    created_by=random.choice(users_from_db),
                    customer=random.choice(customers_from_db),
                    tenant=tenant_from_db[0],
                )
                offer.products.set(random.sample(product_from_db, random.randint(1, 6)))
            messages.add_message(
                request,
                messages.SUCCESS,
                "Offers are successfully added to the database.",
            )
        else:
            messages.add_message(
                request, messages.INFO, "Offers already exist in the database."
            )

        if not Invoice.objects.exists():
            offers_ids = random.sample(range(1, 26), 15)
            offers_from_db = list(Offer.objects.filter(pk__in=offers_ids))
            for i, offer_from_db in enumerate(offers_from_db):
                invoice_statuses = [
                    ("sent", "Sent"),
                    ("paid", "Paid"),
                    ("overdue", "Overdue"),
                    ("canceled", "Canceled"),
                    ("refunded", "Refunded"),
                    ("failed", "Failed"),
                ]

                date_created = fake.date_time_between(
                    start_date=offer_from_db.date_created, end_date="now"
                )
                valid_to_values = [0, 10, 15, 30, 45, 60]
                valid_to = date_created + timedelta(days=random.choice(valid_to_values))
                invoice_number = f"I-{date_created.year}{date_created.month:02d}-{str(i + 1).zfill(3)}"

                invoice = Invoice.objects.create(
                    invoice_number=invoice_number,
                    status=random.choice(invoice_statuses)[0],
                    invoice_note=f"Invoice note for {invoice_number}",
                    date_created=date_created,
                    valid_to=valid_to,
                    tax=25.00,
                    created_by=random.choice(users_from_db),
                    customer=offer_from_db.customer,
                    tenant=tenant_from_db[0],
                    offer=offer_from_db,
                )
                invoice.products.set(offer_from_db.products.all())

            messages.add_message(
                request,
                messages.SUCCESS,
                "Invoices are successfully added to the database.",
            )
        else:
            messages.add_message(
                request, messages.INFO, "Invoices already exist in the database."
            )

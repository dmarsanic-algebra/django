from django.test import TestCase
from .models import Product


# Create your tests here.
class ProductModelTest(TestCase):
    def test_string_representation(self):
        product = Product(name="Test Product")
        self.assertEqual(str(product), product.name)

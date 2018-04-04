from django.test import TestCase
from .models import Product

class ProductPriceTests(TestCase):
		"""docstring for ProductPriceTests"""
		def testPrice(self):
			product_test_price = Product(price=12.0).price
			product_test_price_int = int(Product(price=12.0).price)

			self.assertEqual(product_test_price == product_test_price_int, True)
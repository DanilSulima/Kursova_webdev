from django.test import TestCase
from getfood.models import Provider, Consumer, Category, Product, Store, Order, OrderProduct

class ProviderTestCase(TestCase):
    def setUp(self):
        self.provider = Provider.objects.create(name='John Doe', phone='123-456-7890', rating=4)

    def test_provider_str_method(self):
        self.assertEqual(str(self.provider), 'John Doe')

class ConsumerTestCase(TestCase):
    def setUp(self):
        self.consumer = Consumer.objects.create(name='Jane Doe', phone='987-654-3210', address='Some Address', geo_location='123.456,789.012')

    def test_consumer_str_method(self):
        self.assertEqual(str(self.consumer), 'Jane Doe')

class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Food')

    def test_category_str_method(self):
        self.assertEqual(str(self.category), 'Food')

class ProductTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Food')
        self.product = Product.objects.create(name='Pizza', category=self.category)

    def test_product_str_method(self):
        self.assertEqual(str(self.product), 'Pizza (Food)')






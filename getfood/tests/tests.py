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

class StoreTestCase(TestCase):
    def setUp(self):
        self.provider = Provider.objects.create(name='John Doe', phone='123-456-7890', rating=4)
        self.category = Category.objects.create(name='Food')
        self.product = Product.objects.create(name='Pizza', category=self.category)
        self.store = Store.objects.create(provider=self.provider, product=self.product, price=10.99)

    def test_store_str_method(self):
        self.assertEqual(str(self.store), 'John Doe\'s Pizza Store')

class OrderTestCase(TestCase):
    def setUp(self):
        self.consumer = Consumer.objects.create(name='Jane Doe', phone='987-654-3210', address='Some Address', geo_location='123.456,789.012')
        self.order = Order.objects.create(consumer=self.consumer, status='new')

    def test_order_str_method(self):
        self.assertEqual(str(self.order), 'Order #1')

class OrderProductTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Food')
        self.product = Product.objects.create(name='Pizza', category=self.category)
        self.consumer = Consumer.objects.create(name='Jane Doe', phone='987-654-3210', address='Some Address', geo_location='123.456,789.012')
        self.order = Order.objects.create(consumer=self.consumer, status='new')
        self.order_product = OrderProduct.objects.create(product=self.product, order=self.order, amount=2)

    def test_order_product_str_method(self):
        self.assertEqual(str(self.order_product), 'Pizza (Food) - Quantity: 2')

from django.test import TestCase
from django.urls import reverse
from django.utils import archive
from shopapp.models import Product
from shopapp.utils import add_two_numbers
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from string import ascii_letters
from random import choices

from django.conf import settings



class AddTwoNumbersTestCase(TestCase):
    def test_add_two_numbers(self):
        result = add_two_numbers(3, 8)
        self.assertEqual(result, 11)

# class UserCreationTestCase(TestCase):
#     @classmethod
#     def create_test_user(cls):
#         # Create an admin user
#         return User.objects.create_superuser(username='admin', email='admin@example.com', password='admin')

class ProductCreateViewTestCase(TestCase):
    def setUp(self) -> None:
        # self.admin_user = UserCreationTestCase.create_test_user()
        self.product_name = "".join(choices(ascii_letters, k=10))
        Product.objects.filter(name=self.product_name).delete
        self.admin_user = User.objects.create_superuser(username='admin', email='admin@example.com', password='<PASSWORD>')

    def test_product_create_view(self):
        # Log in the admin user
        self.client.force_login(self.admin_user)

        # Make the POST request to create a product
        response = self.client.post(
            reverse('shopapp:product_create'),
            {
                'name': self.product_name,
                'price': 100,
                'description': 'test description',
                'discount': 0,
            }
        )

        # Check if the response redirects to the product list page
        self.assertRedirects(response, reverse('shopapp:products_list'))
        self.assertTrue(
            Product.objects.filter(name=self.product_name).exists()
        )

class ProductDetailsViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.product = Product.objects.create(name="Best Product")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.product.delete()

    # def setUp(self) -> None:
    #     self.product = Product.objects.create(name="Best Product")
    
    # def tearDown(self) -> None:
    #     self.product.delete()

    def test_get_product_(self):
        response = self.client.get(
            reverse("shopapp:product_details", kwargs={"pk": self.product.pk})
        )
        self.assertEqual(response.status_code, 200)

    
    def test_get_product_and_check_content(self):
        response = self.client.get(
            reverse("shopapp:product_details", kwargs={"pk": self.product.pk})
        )
        self.assertContains(response, self.product.name)


class ProductsListViewTestCase(TestCase):
    fixtures = [
        'products-fixture.json',
    ]

    def test_products(self):
        response = self.client.get(reverse('shopapp:products_list'))
        self.assertQuerysetEqual(
            qs=Product.objects.filter(archived=False).all(),
            values=(p.pk for p in response.context['products']),
            transform=lambda p: p.pk,
        )
        self.assertTemplateUsed(response,'shopapp/products-list.html')

        # response = self.client.get(reverse('shopapp:products_list'))
        # products = Product.objects.filter(archived=False).all()
        # products_ = response.context['products']
        # for p,p_ in zip(products, products_):
        #     self.assertEqual(p.pk, p_.pk)
        # for product in Product.objects.filter(archived=False).all():
        #     self.assertContains(response, product.name)
    


class OrdersListViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.credentials = dict(username='testuser', password='<PASSWORD>')
        cls.user = User.objects.create_user(username='testuser', password='<PASSWORD>')

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_orders_view(self):
        response = self.client.get(reverse('shopapp:orders_list'))
        self.assertContains(response, 'Orders')
    
    def test_orders_view_not_authenticated(self):
        self.client.logout()
        response = self.client.get(reverse('shopapp:orders_list'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(str(settings.LOGIN_URL), response.url)


class ProductsExportViewTestCase(TestCase):
    fixtures = [
        'products-fixture.json',
    ]

    def test_get_products_view(self):
        response = self.client.get(reverse('shopapp:products_export'))
        self.assertEqual(response.status_code, 200)
        products = Product.objects.order_by("pk").all()
        expected_data = [
            {
                'pk': product.pk,
                'name': product.name,
                'price': str(product.price),
                'archived': product.archived,
            }
            for product in products
        ]

        products_data = response.json()
        self.assertEqual(products_data["products"], expected_data)

# python manage.py dumpdata shopapp > shopapp-fixtures.json
# python manage.py loaddata shopapp-fixtures.json
# python manage.py dumpdata shopapp.Product > shopapp/fixtures/products-fixture.json
# Shift + Alt + F  
# python manage.py test shopapp.tests.ProductsListViewTestCase

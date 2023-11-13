from rest_framework.test import APITestCase
from django.urls import reverse
from apps.users import factories as user_factories
from apps.product import factories as product_factories


class UsersAPITestCase(APITestCase):
    def setUp(self):
        self.super_user = user_factories.UserFactory(is_superuser=True)
        self.employee = user_factories.EmployeeFactory()
        self.clnt = user_factories.ClientFactory()
        self.product = product_factories.ProductFactory(quantity=10)
        self.order = product_factories.OrderFactory(employee=self.employee, client=self.clnt)
        product_factories.OrderProductFactory(order=self.order, product=self.product, quantity=3)

    def test_employee_list_statistics(self):
        self.client.force_login(self.super_user)
        response = self.client.get(reverse('users:employee-statistics-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_employee_detail_statistics(self):
        self.client.force_login(self.super_user)
        response = self.client.get(reverse('users:employee-statistics', kwargs={'pk': self.employee.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['client_count'], 1)
        self.assertEqual(response.data['total_product_count'], 3)
        self.assertEqual(response.data['total_order_sum'], str(self.order.total_price))

    def test_client_detail_statistics(self):
        self.client.force_login(self.super_user)
        response = self.client.get(reverse('users:client-statistics', kwargs={'pk': self.clnt.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['total_bought_product_count'], 3)
        self.assertEqual(response.data['total_order_sum'], str(self.order.total_price))

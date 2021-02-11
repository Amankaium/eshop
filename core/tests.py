from django.test import TestCase, Client
from django.urls import reverse


class OrderTestCase(TestCase):
    def test_success_open_order_add_page(self):
        client = Client()
        response = client.get("/order/all/")
        self.assertEqual(response.data, [])
        self.assertEqual(response.status_code, 200)

    def test_order_retrive_not_authorized(self):
        client = Client()
        response = client.get(reverse("order", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 401)


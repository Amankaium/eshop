from django.test import TestCase, Client


class OrderAddTestCase(TestCase):
    def test_success_open_order_add_page(self):
        client = Client()
        response = client.get("/order/all/")
        self.assertEqual(response.data, [])
        self.assertEqual(response.status_code, 200)
    
from django.test import TestCase, Client
from django.urls import reverse
from .models import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


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


class CategoryListTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("category-list")

    def test_success_get_category_list(self):
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, 200)
    
    def test_success_get_two_categories(self):
        category_1 = Category.objects.create(name="Мыломоющие")

        category_2 = Category()
        category_2.name = "Молочные"
        category_2.save()

        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)


class CategoryListSeleniumTestCase(TestCase):
    def test_success_makecategories(self):
        driver = webdriver.Chrome()
        
        driver.get("http://localhost:8000/admin/")
        
        elem = driver.find_element_by_name("username")
        elem.clear()
        elem.send_keys("admin@gmail.com")

        elem = driver.find_element_by_name("password")
        elem.clear()
        elem.send_keys("admin")

        elem.send_keys(Keys.RETURN)
        sleep(3)

        categories = driver.find_element_by_link_text("Categorys")
        categories.click()

        driver.find_elements_by_class_name("addlink")[-1].click()

        caterory_1 = "Напитки"
        driver.find_element_by_name("name").send_keys(caterory_1)
        driver.find_elements_by_tag_name("input")[-2].click()

        caterory_2 = "Сладости"
        driver.find_element_by_name("name").send_keys(caterory_2)
        driver.find_elements_by_tag_name("input")[-3].click()

        sleep(3)

        driver.get("http://localhost:8000/category/")
        self.assertIn(caterory_1, driver.page_source)
        self.assertIn(caterory_2, driver.page_source)

        sleep(5)
        driver.close()

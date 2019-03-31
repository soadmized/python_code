#from django.test import TestCase

# Create your tests here.

from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_aboutpage_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

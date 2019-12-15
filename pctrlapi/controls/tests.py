import json
import os
from django.conf import settings
from django.urls import reverse
from django.test import Client
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Control
from .serializers import ControlSerializer

data = {
        "data": {
            "type": "Control",
            "id": "1",
            "attributes": {
                "name": "test",
                "type": "Primitive",
                "maximum_rabi_rate": 43.0,
                "polar_angle": 0.92
            }
        }
    }

class ControlListAPIViewTestCase(APITestCase):
    url = reverse("list")

    def test_create_control(self):
        """
        Ensure we can create a new control object.
        """
        response = self.client.post(self.url, data, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Control.objects.count(), 1)
        self.assertEqual(Control.objects.get().name, 'test')

    def test_list_controls(self):
        """
        Test to verify control list
        """
        Control.objects.create(name='test',
                                type='Primitive',
                                maximum_rabi_rate=43.0,
                                polar_angle=0.92
                            )
        response = self.client.get(self.url)
        self.assertTrue(len(json.loads(response.content).get('data')) == Control.objects.count())

class ControlDetailAPIViewTestCase(APITestCase):

    def setUp(self):
        self.control = Control.objects.create(name='test',
                                                type='Primitive',
                                                maximum_rabi_rate=43.0,
                                                polar_angle=0.92
                                            )
        self.url = reverse("detail", kwargs={'pk': self.control.id})

    def test_get_control(self):
        """
        Ensure we can get a specific control object.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(data.get('data').get('attributes'), response_data.get('data').get('attributes'))
    
    def test_update_control(self):
        """
        Ensure we can update a specific control object.
        """
        new_data = {
                    "data": {
                        "type": "Control",
                        "id": "1",
                        "attributes": {
                            "name": "new_test",
                            "type": "Primitive",
                            "maximum_rabi_rate": 43.0,
                            "polar_angle": 0.92
                        }
                    }
                }
        response = self.client.put(self.url, new_data, format='vnd.api+json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        control = Control.objects.get(id=self.control.id)
        self.assertEqual(control.name, "new_test")
        self.assertEqual(control.name, response_data
                                        .get("data")
                                        .get("attributes")
                                        .get("name"))

    def test_control_delete(self):
        """
        Ensure we can delete a specific control object.
        """
        response = self.client.delete(self.url)
        self.assertEqual(204, response.status_code)

class ControlListCSVAPIViewTestCase(APITestCase):
    url = reverse("listcsv")

    def test_export(self):
        """
        Ensure we can download controls as a CSV file.
        """
        self.control = Control.objects.create(name='test',
                                                type='Primitive',
                                                maximum_rabi_rate=43.0,
                                                polar_angle=0.92
                                            )
        response = self.client.get(self.url)
        self.assertEquals(
            response.get('Content-Disposition'),
                "attachment; filename=\"controls.csv\""
            )
        self.assertEquals(response.content,
                b'maximum_rabi_rate,name,polar_angle,type\r\n43.0,test,0.92,Primitive\r\n')

    def test_invalid_import(self):
        """
        Ensure upload fails if invalid file is uploaded.
        e.g. a row that has type "Primitiv" (where only "Primitive" is allowed).
        """
        c = Client()
        dir = os.path.join(settings.BASE_DIR)
        with open(dir + '/controls/test_assets/test_invalid.csv', 'rb') as f:
            response = c.post(self.url, data={'file': f}, format='text/csv')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Control.objects.count(), 0)

    def test_import(self):
        """
        Ensure we can bulk upload controls as a CSV file.
        """
        c = Client()
        dir = os.path.join(settings.BASE_DIR)
        with open(dir + '/controls/test_assets/test.csv', 'rb') as f:
            response = c.post(self.url, data={'file': f}, format='text/csv')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Control.objects.count(), 3)

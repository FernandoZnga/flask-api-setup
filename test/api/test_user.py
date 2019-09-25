import unittest
import json

from server import server
from models.abc import db
from models import User


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = server.test_client()

    def setUp(self):
        db.create_all()
        User('Jimmy', 'Fallon', 99).save()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get(self):
        response = self.client.get(
            '/application/user',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_json, [
            {
                'age': 99,
                'first_name': 'Jimmy',
                'last_name': 'Fallon'
            },
        ])
    
    def test_post(self):
        response = self.client.post(
            '/application/user',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_json, [
            {
                'age': 99,
                'first_name': 'Jimmy',
                'last_name': 'Fallon'
            },
        ])

    def test_put(self):
        response = self.client.put(
            '/application/user',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_json, [
            {
                'age': 99,
                'first_name': 'Jimmy',
                'last_name': 'Fallon'
            },
        ])

    def test_delete(self):
        response = self.client.delete(
            '/application/user',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_json, [
            {
                'first_name': 'Jimmy',
                'last_name': 'Fallon'
            },
        ])
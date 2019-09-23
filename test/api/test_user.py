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
        User('John', 'Doe', 25).save()

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
                'age': 25,
                'first_name': 'John',
                'last_name': 'Doe'
            },
        ])
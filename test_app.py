import unittest
from unittest import mock

from fastapi.testclient import TestClient

from api import app
import pokemon_functions


class TestApi(unittest.TestCase):
    """Test class for api.py."""

    CLIENT = TestClient(app)

    def test_01_hello_world(self):
        """Test function for hello-world function."""
        response = self.CLIENT.get("/hello-world")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'msg': 'Hello World!'})

    @mock.patch('api.pokemon_functions.get_pokemon_data')
    def test_02_get_pokemon(self, _):
        """Test function for get_pokemon function."""

        # Missing parameter case
        response = self.CLIENT.get("/pokemon")
        self.assertEqual(response.status_code, 422)

        # Pokemon not found
        _.return_value = {"status_code": 404, "error": "Not Found!"}
        response = self.CLIENT.get("/pokemon?pokemon_name=123123123")
        self.assertEqual(response.status_code, 404)

        # Existing one
        _.return_value = {"status_code": 200, "data": []}
        response = self.CLIENT.get("/pokemon?pokemon_name=ditto")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()

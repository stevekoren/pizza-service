import unittest

from fastapi.testclient import TestClient
from app.main import app
import json
import httpx
import pytest

client = TestClient(app)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_health(self):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "OK"}

    def test_create_order(self):
        # Define a valid order
        order = {
            "piza-type": "margarita",
            "size": "personal",
            "amount": 2
        }

        response = client.post("/order", data=json.dumps(order))
        assert response.status_code == 200

        # Check the response JSON
        response_data = response.json()
        assert "order_id" in response_data
        assert response_data["piza_type"] == order["piza_type"]
        assert response_data["size"] == order["size"]
        assert response_data["amount"] == order["amount"]


if __name__ == '__main__':
    unittest.main()

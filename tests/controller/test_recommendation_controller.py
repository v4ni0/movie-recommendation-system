import unittest
from fastapi.testclient import TestClient

from src.controller.recommendation_controller import app

class TestMovieRecommendationAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_when_valid_request_provided_then_endpoint_returns_200_and_recommendations(self):
        response = self.client.get("/recommend", params={"description": "Space travel and aliens", "top_k": 3})
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn("recommendations", data)
        self.assertEqual(len(data["recommendations"]), 3)

        first_rec = data["recommendations"][0]
        self.assertIn("id", first_rec)
        self.assertIn("title", first_rec)
        self.assertIn("score", first_rec)

    def test_when_top_k_is_omitted_then_endpoint_uses_default_top_k(self):
        response = self.client.get("/recommend", params={"description": "Romantic comedy"})
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn("recommendations", data)
        self.assertTrue(len(data["recommendations"]) > 0)

    def test_when_empty_description_provided_then_endpoint_returns_400(self):
        response = self.client.get("/recommend", params={"description": "   ", "top_k": 5})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], "Please provide a valid query.")

    def test_when_description_is_missing_then_endpoint_returns_422_validation_error(self):
        response = self.client.get("/recommend", params={"top_k": 5})

        self.assertEqual(response.status_code, 422)

from django.test import TestCase
from rest_framework.test import APIClient

class EndpointTests(TestCase):

    def test_predict_view(self):
        client = APIClient()
        input_data = {
            "age": 37,
            "workclass": "Private",
            "fnlwgt": 34146,
            "education": "HS-grad",
            "education-num": 9,
            "marital-status": "Married-civ-spouse",
            "occupation": "Craft-repair",
            "relationship": "Husband",
            "race": "White",
            "sex": "Male",
            "capital-gain": 0,
            "capital-loss": 0,
            "hours-per-week": 68,
            "native-country": "United-States"
        }
        classifier_url = "/api/v1/income_classifier/predict"
        response = client.post(classifier_url, input_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["label"], "<=50K")
        self.assertTrue("request_id" in response.data)
        self.assertTrue("status" in response.data)

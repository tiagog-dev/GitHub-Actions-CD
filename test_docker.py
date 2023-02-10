import unittest
import requests
from deepdiff import DeepDiff


class TestPricePrediction(unittest.TestCase):
    def test_price_prediction(self):
        # Define the API endpoint
        URL = "http://0.0.0.0:8000/predict"

        # Define the car data for the prediction
        car = {
            "model": "Fiesta",
            "year": 2019,
            "transmission": "Manual",
            "mileage": 14337,
            "fuelType": "Petrol",
            "mpg": 58.9,
            "engineSize": 1,
        }

        # Make a POST request to the API with the car data
        response = requests.post(URL, json=car)

        # Check that the request was successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Get the expected prediction result
        expected_response = {"Ford car price suggested": 11620}

        # Check that the response is as expected
        difference = DeepDiff(expected_response, response.json(), ignore_order=True)
        self.assertEqual(difference, {})


if __name__ == "__main__":
    unittest.main()

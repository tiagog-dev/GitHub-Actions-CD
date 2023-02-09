import requests

URL = "http://0.0.0.0:8000/predict"

car = {
    "model": "Fiesta",
    "year": 2019,
    "transmission": "Manual",
    "mileage": 14337,
    "fuelType": "Petrol",
    "mpg": 58.9,
    "engineSize": 1
}

response = requests.post(URL, json=car)
prediction = response.json()

print("Car price prediction: ", prediction)
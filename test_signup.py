import requests

url = "http://127.0.0.1:5000/signup"

data = {
    "name": "Test Student",
    "email": "teststudent@example.com",
    "password": "TestPass123"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())
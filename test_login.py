import requests

url = "http://127.0.0.1:5000/login"

email = input("Enter Email: ")
password = input("Enter Password: ")

data = {
    "email": email,
    "password": password
}

response = requests.post(url, json=data)

print("\nStatus Code:", response.status_code)
print("Response:", response.json())
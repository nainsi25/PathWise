import requests

session = requests.Session()

# Login
login_url = "http://127.0.0.1:5000/login"

data = {
    "email": "teststudent@example.com",
    "password": "TestPass123"
}

login_response = session.post(login_url, json=data)

print("LOGIN:")
print("Status Code:", login_response.status_code)
print("Response:", login_response.json())


# Logout
logout_url = "http://127.0.0.1:5000/logout"

logout_response = session.post(logout_url)

print("\nLOGOUT:")
print("Status Code:", logout_response.status_code)
print("Response:", logout_response.json())
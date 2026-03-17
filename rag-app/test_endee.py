import requests

response = requests.get("http://localhost:8080")
print("Status Code:", response.status_code)
print("Response:")
print(response.text[:500])
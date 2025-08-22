import os
import requests

API_KEY = "12e7be1a52a00b5acf03d72824f9355b"
url = "https://gnews.io/api/v4/search"
params = {"q": "politics", "lang": "en", "max": 10, "apikey": API_KEY}

response = requests.get(url, params=params)
print("Status:", response.status_code)
print("Response:", response.json())

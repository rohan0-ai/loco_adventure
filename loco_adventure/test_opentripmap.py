import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENTRIPMAP_API_KEY")

url = "https://api.opentripmap.com/0.1/en/places/radius"

params = {
    "radius": 5000,
    "lon": 77.2090,      # India Gate
    "lat": 28.6139,
    "limit": 5,
    "apikey": API_KEY,
}

response = requests.get(url, params=params, timeout=10)

print("Status:", response.status_code)
print(response.json())
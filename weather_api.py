import requests
import time
import json
from .config import BASE_URL, API_KEY, CACHE_DIR, CACHE_DURATION

def read_cache(name: str):
    file = CACHE_DIR / f"{name}.json"
    if file.exists():
        if time.time() - file.stat().st_mtime < CACHE_DURATION:
            try:
                with open(file, "r") as f:
                    return json.load(f)
            except:
                return None
    return None

def write_cache(name: str, data):
    file = CACHE_DIR / f"{name}.json"
    try:
        with open(file, "w") as f:
            json.dump(data, f, indent=2)
    except:
        pass

def fetch_data(endpoint: str, city: str):
    cache_name = f"{endpoint}_{city}"
    cached = read_cache(cache_name)
    if cached:
        return cached, True

    try:
        response = requests.get(
            f"{BASE_URL}/{endpoint}",
            params={"q": city, "appid": API_KEY, "units": "metric"},
            timeout=10,
        )
        data = response.json()

        if response.status_code == 200:
            write_cache(cache_name, data)
            return data, False
        else:
            print("API error:", data.get("message", "Unknown error"))
    except requests.RequestException as e:
        print("Network error:", e)

    return None, False

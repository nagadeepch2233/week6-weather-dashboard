from pathlib import Path
import json

API_KEY = "Type your API Key here"  
BASE_URL = "https://api.openweathermap.org/data/2.5"
CACHE_DIR = Path("weather_cache")
CACHE_DIR.mkdir(exist_ok=True)
CACHE_DURATION = 600 

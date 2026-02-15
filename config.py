from pathlib import Path
import json

API_KEY = "f8a559765b3c778b654acfd85645d644"  
BASE_URL = "https://api.openweathermap.org/data/2.5"
CACHE_DIR = Path("weather_cache")
CACHE_DIR.mkdir(exist_ok=True)
CACHE_DURATION = 600 

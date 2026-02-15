from .weather_display import display_dashboard
from .config import CACHE_DIR, API_KEY

def main():
    city = "Hyderabad"

    while True:
        display_dashboard(city)
        cmd = input("Type 'refresh', 'search', or 'quit': ").strip().lower()

        if cmd == "refresh":
            for f in CACHE_DIR.glob("*.json"):
                f.unlink()
        elif cmd == "search":
            new_city = input("Enter city name: ").strip()
            if new_city:
                city = new_city
        elif cmd == "quit":
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    if not API_KEY:
        print("Please set OPENWEATHER_API_KEY in your environment.")
    else:
        main()

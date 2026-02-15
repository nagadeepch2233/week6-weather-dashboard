from datetime import datetime
from .weather_api import fetch_data
from .weather_parser import get_emoji, wind_dir, parse_forecast

def display_dashboard(city: str):
    weather, cached_weather = fetch_data("weather", city)
    forecast_data, cached_forecast = fetch_data("forecast", city)

    if not weather or not forecast_data:
        print("Unable to retrieve data.")
        return

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n🌤️  WEATHER DASHBOARD")
    print("=" * 30)
    print(f"\n📍 Current Location: {weather['name']}, {weather['sys']['country']}")
    print(f"🕐 Last Updated: {now}\n")

    main = weather.get("main", {})
    wind = weather.get("wind", {})
    sys = weather.get("sys", {})
    desc = weather.get("weather", [{}])[0].get("description", "N/A")

    print("Current Weather:")
    print("─" * 30)
    print(f"Temperature:   {round(main.get('temp',0))}°C (Feels like: {round(main.get('feels_like',0))}°C)")
    print(f"Conditions:    {desc.title()} {get_emoji(desc)}")
    print(f"Humidity:      {main.get('humidity',0)}%")
    print(f"Wind:          {round(wind.get('speed',0)*3.6)} km/h from {wind_dir(wind.get('deg',0))}")
    print(f"Pressure:      {main.get('pressure',0)} hPa")
    print(f"Visibility:    {round(weather.get('visibility',0)/1000)} km")
    print(f"Sunrise:       {datetime.fromtimestamp(sys.get('sunrise',0)).strftime('%H:%M')}")
    print(f"Sunset:        {datetime.fromtimestamp(sys.get('sunset',0)).strftime('%H:%M')}\n")

    print("5-Day Forecast:")
    print("─" * 30)

    forecast = parse_forecast(forecast_data)
    for day in forecast:
        print(
            f"{day['day']}: {get_emoji(day['description'])}   "
            f"{day['max_temp']}°C / {day['min_temp']}°C  "
            f"(Humidity: {day['humidity']}%)"
        )

    print(f"\nAPI Status: {'Using cached data' if cached_weather or cached_forecast else 'Live data'}")

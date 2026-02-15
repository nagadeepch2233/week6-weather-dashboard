from datetime import datetime

def get_emoji(description: str) -> str:
    desc = description.lower()
    if "rain" in desc:
        return "🌧️"
    if "cloud" in desc:
        return "☁️"
    if "clear" in desc:
        return "☀️"
    if "snow" in desc:
        return "❄️"
    return "⛅"

def wind_dir(degrees: int) -> str:
    dirs = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    return dirs[int((degrees + 22.5) // 45) % 8]

def parse_forecast(forecast_data):
    daily = {}
    for item in forecast_data.get("list", []):
        date = item["dt_txt"].split()[0]
        daily.setdefault(date, []).append(item)

    parsed = []
    for i, date in enumerate(daily):
        temps = [x["main"]["temp"] for x in daily[date]]
        hums = [x["main"]["humidity"] for x in daily[date]]
        desc = daily[date][0]["weather"][0]["description"]
        day = datetime.strptime(date, "%Y-%m-%d").strftime("%a %d %b")

        parsed.append({
            "day": day,
            "description": desc,
            "max_temp": round(max(temps)),
            "min_temp": round(min(temps)),
            "humidity": round(sum(hums) / len(hums)),
        })

        if i == 4:
            break

    return parsed

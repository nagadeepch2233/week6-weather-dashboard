from weather_app.weather_parser import get_emoji, wind_dir, parse_forecast

def test_get_emoji():
    assert get_emoji("light rain") == "🌧️"
    assert get_emoji("clear sky") == "☀️"
    assert get_emoji("snow") == "❄️"
    assert get_emoji("few clouds") == "☁️"

def test_wind_dir():
    assert wind_dir(0) == "N"
    assert wind_dir(90) == "E"
    assert wind_dir(180) == "S"
    assert wind_dir(270) == "W"

def test_parse_forecast():
    sample_data = {
        "list": [
            {
                "dt_txt": "2026-02-15 12:00:00",
                "main": {"temp": 25, "humidity": 60},
                "weather": [{"description": "clear sky"}],
            },
            {
                "dt_txt": "2026-02-15 18:00:00",
                "main": {"temp": 20, "humidity": 70},
                "weather": [{"description": "clear sky"}],
            },
        ]
    }

    result = parse_forecast(sample_data)

    assert len(result) == 1
    assert result[0]["max_temp"] == 25
    assert result[0]["min_temp"] == 20
    assert result[0]["humidity"] == 65

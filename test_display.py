from unittest.mock import patch
from weather_app.weather_display import display_dashboard

@patch("weather_app.weather_display.fetch_data")
def test_display_dashboard(mock_fetch, capsys):
    mock_fetch.side_effect = [
        (
            {
                "name": "TestCity",
                "sys": {"country": "TC", "sunrise": 0, "sunset": 0},
                "main": {"temp": 25, "feels_like": 24, "humidity": 60, "pressure": 1012},
                "wind": {"speed": 5, "deg": 90},
                "visibility": 10000,
                "weather": [{"description": "clear sky"}],
            },
            False,
        ),
        (
            {
                "list": [
                    {
                        "dt_txt": "2026-02-15 12:00:00",
                        "main": {"temp": 25, "humidity": 60},
                        "weather": [{"description": "clear sky"}],
                    }
                ]
            },
            False,
        ),
    ]

    display_dashboard("TestCity")
    captured = capsys.readouterr()

    assert "WEATHER DASHBOARD" in captured.out
    assert "TestCity" in captured.out

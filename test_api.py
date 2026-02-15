import pytest
from unittest.mock import patch, MagicMock
from weather_app.weather_api import fetch_data

@patch("weather_app.weather_api.requests.get")
def test_fetch_data_success(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"name": "TestCity"}
    mock_get.return_value = mock_response

    data, cached = fetch_data("weather", "TestCity")

    assert data["name"] == "TestCity"
    assert cached is False

@patch("weather_app.weather_api.requests.get")
def test_fetch_data_api_error(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_response.json.return_value = {"message": "city not found"}
    mock_get.return_value = mock_response

    data, cached = fetch_data("weather", "InvalidCity")

    assert data is None
    assert cached is False

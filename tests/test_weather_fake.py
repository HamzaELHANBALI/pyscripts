from pyscripts.weather_fake import get_fake_weather


def test_get_fake_weather_known_city():
    assert get_fake_weather("Toulouse") == "soleil"


def test_get_fake_weather_unknown_city():
    assert get_fake_weather("Lyon") == "meteo inconnue"

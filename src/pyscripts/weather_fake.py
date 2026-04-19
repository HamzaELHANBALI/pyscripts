"""Donnees meteo fictives pour les exercices."""

FAKE_WEATHER = {
    "toulouse": "soleil",
    "montpellier": "vent",
    "paris": "nuages",
}


def get_fake_weather(city: str) -> str:
    key = city.strip().lower()
    return FAKE_WEATHER.get(key, "meteo inconnue")

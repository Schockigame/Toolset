import os
import sys
import requests

def get_weather(city, api_key):
    """
    Ruft das aktuelle Wetter für eine Stadt über die OpenWeatherMap API ab.
    """
    # API-URL
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric', # Für Celsius
        'lang': 'de'
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status() # Löst einen Fehler bei schlechtem Statuscode aus
        
        data = response.json()
        
        # Extrahiere die relevanten Informationen
        city_name = data['name']
        description = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        # Gib das Wetter in einem schönen Format aus
        print("--- Aktuelles Wetter ---")
        print(f"📍 Stadt:    {city_name}")
        print(f"☀️ Wetter:   {description}")
        print(f"🌡️ Temp.:    {temp}°C (Gefühlt wie {feels_like}°C)")
        print(f"💧 Feucht.:  {humidity}%")
        print(f"💨 Wind:     {wind_speed} m/s")
        print("------------------------")

    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            print(f"Fehler: Stadt '{city}' nicht gefunden.")
        elif response.status_code == 401:
            print("Fehler: Ungültiger API-Schlüssel. Bitte überprüfe ihn.")
        else:
            print(f"HTTP Fehler: {err}")
    except Exception as err:
        print(f"Ein Fehler ist aufgetreten: {err}")

if __name__ == "__main__":
    # API-Schlüssel aus einer Umgebungsvariable lesen
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    
    if not API_KEY:
        print("Fehler: Der API-Schlüssel wurde nicht gefunden.")
        print("Bitte setze die Umgebungsvariable 'OPENWEATHER_API_KEY'.")
        sys.exit(1)
        
    if len(sys.argv) < 2:
        print("Benutzung: python weather.py <Stadtname>")
        sys.exit(1)
        
    # Erlaube Städtenamen mit Leerzeichen
    city_query = " ".join(sys.argv[1:])
    get_weather(city_query, API_KEY)
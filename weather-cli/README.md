# Command-Line Weather

Ein CLI-Tool, um das aktuelle Wetter für eine Stadt direkt im Terminal anzuzeigen. Es verwendet die API von [OpenWeatherMap](https://openweathermap.org/).

## Einrichtung

1.  **API-Schlüssel erhalten:**
    * Registriere dich kostenlos auf [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).
    * Navigiere zum Tab "API keys" und kopiere deinen Schlüssel.

2.  **API-Schlüssel als Umgebungsvariable setzen:**
    Das Skript liest den Schlüssel sicher aus einer Umgebungsvariable.

    * **Linux/macOS:**
        ```bash
        export OPENWEATHER_API_KEY="DEIN_API_SCHLÜSSEL_HIER"
        # Um es permanent zu machen, füge diese Zeile zu deiner .bashrc oder .zshrc hinzu.
        ```
    * **Windows:**
        ```powershell
        $env:OPENWEATHER_API_KEY="DEIN_API_SCHLÜSSEL_HIER"
        ```

3.  **Abhängigkeiten installieren:**
    ```bash
    pip install -r requirements.txt
    ```

## Benutzung

Führe das Skript mit dem Namen der Stadt aus.
```bash
python weather.py Berlin
python weather.py "New York"
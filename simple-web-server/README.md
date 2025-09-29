# Simple Web Server

Dieses Skript startet einen einfachen, lokalen Webserver in dem Verzeichnis, in dem es ausgeführt wird. Es ist ein Wrapper um Pythons eingebautes `http.server`-Modul.

## Benutzung

1.  **Navigiere** in den Ordner mit deinen HTML/CSS/JS-Dateien.
2.  **Kopiere** das `server.py` Skript in diesen Ordner (oder rufe es mit dem vollen Pfad auf).
3.  **Führe das Skript aus:**

    ```bash
    # Startet den Server auf dem Standard-Port 8000
    python server.py
    ```
    ```
    # Startet den Server auf einem anderen Port (z.B. 8080)
    python server.py 8080
    ```
4.  Öffne deinen Browser und gehe zu `http://localhost:8000` (oder dem von dir gewählten Port).

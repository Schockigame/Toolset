# YouTube Transcript Downloader

Dieses Skript lädt das automatisch generierte oder manuell hinzugefügte Transkript eines YouTube-Videos herunter und speichert es als Textdatei.

## Benutzung

1.  **Abhängigkeiten installieren:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Skript ausführen:**
    Gib die URL des YouTube-Videos als Argument an. Setze die URL in Anführungszeichen, um Fehler mit Sonderzeichen zu vermeiden.
    ```bash
    python get_transcript.py "[https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://www.youtube.com/watch?v=dQw4w9WgXcQ)"
    ```
    Das Skript erstellt eine Datei wie `dQw4w9WgXcQ_transcript.txt` im selben Ordner.
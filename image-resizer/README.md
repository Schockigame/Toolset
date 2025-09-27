# Image Resizer

Dieses Python-Skript verkleinert alle Bilder in einem angegebenen Ordner auf eine maximale Breite/Höhe und speichert sie in einem neuen Unterordner namens `resized`.

## Benutzung

1.  **Abhängigkeiten installieren:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Skript ausführen:**
    Navigiere in das Verzeichnis und führe das Skript mit dem Pfad zu deinem Bilderordner aus.

    ```bash
    # Standardgröße (max. 1024 Pixel)
    python resize_images.py "/Pfad/zu/deinen/Bildern"

    # Eigene Größe angeben (z.B. max. 800 Pixel)
    python resize_images.py "/Pfad/zu/deinen/Bildern" 800
    ```
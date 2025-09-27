# Dotfile Backup Script

Ein einfaches Bash-Skript, um wichtige Konfigurationsdateien (Dotfiles) aus deinem Home-Verzeichnis in einen zentralen Backup-Ordner zu kopieren.

## Konfiguration

Öffne die Datei `backup.sh` und passe die folgenden Variablen an:

1.  `FILES_TO_BACKUP`: Füge die Namen der Dateien hinzu, die du sichern möchtest.
2.  `DEST_DIR`: Ändere den Pfad, in den die Dateien kopiert werden sollen.

## Benutzung

1.  **Mach das Skript ausführbar:**
    ```bash
    chmod +x backup.sh
    ```

2.  **Führe das Skript aus:**
    ```bash
    ./backup.sh
    ```
# Find Large Files

Ein schnelles Bash-Skript, um die größten Dateien in einem bestimmten Verzeichnis und seinen Unterverzeichnissen zu finden.

## Benutzung

1.  **Mach das Skript ausführbar:**
    ```bash
    chmod +x find_large.sh
    ```

2.  **Führe das Skript aus:**
    ```bash
    # Durchsuche das aktuelle Verzeichnis nach den 10 größten Dateien
    ./find_large.sh

    # Durchsuche ein bestimmtes Verzeichnis (z.B. /var/log)
    ./find_large.sh /var/log

    # Finde die 20 größten Dateien in deinem Home-Verzeichnis
    ./find_large.sh ~ 20
    ```
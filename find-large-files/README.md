# Find Large Files

Ein einfaches und schnelles **Bash-Skript**, um die **größten Dateien** in einem Verzeichnis (inkl. Unterordnern) zu finden.

---

## Features

-  Durchsucht automatisch alle Unterverzeichnisse  
-  Zeigt Dateigrößen in **lesbarer Form** (z. B. `1.2G`, `850M`)  
-  Frei konfigurierbar: **Zielverzeichnis** & **Anzahl der Dateien**

---

## Nutzung
1. **Skript ausführbar machen:**
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

---

## Hinweis

Falls du Fehlermeldungen wie "Zugriff verweigert" bekommst, liegt das meist an fehlenden Berechtigungen.
In diesem Fall kannst du das Skript mit sudo starten:
```bash
sudo ./find_large.sh /root 15
```

---

Beispielausgabe:
```
Suche die 10 größten Dateien in '/var/log'...
-----------------------------------------------------
1.2G    /var/log/biglog1.log
850M    /var/log/old/archive.tar
450M    /var/log/system/journal.log
...
-----------------------------------------------------
Suche abgeschlossen.
```

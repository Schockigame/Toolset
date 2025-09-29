# System Health Dashboard

Ein einfaches Bash-Skript bzw. Powershell-Skript, das eine schnelle Übersicht über die wichtigsten Metriken deines Systems (CPU, RAM, Festplatte) anzeigt.

**Hinweis:** 

Für Linux Systeme lade die `health.sh` datei runter. 

Für Windows lade die `system_report.ps1` datei runter.

## Benutzung Linux

1.  **Mach das Skript ausführbar:**
    ```bash
    chmod +x health.sh
    ```
2.  **Führe es aus:**
    ```bash
    ./health.sh
    ```

## Benutzung Windows

1. **Aktiviere die Nutzung von Skripts**
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ``` 
3.  **Führe es aus:**
    ```powershell
    ./system_report.ps1
    ```

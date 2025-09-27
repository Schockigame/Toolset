#!/bin/bash

# Dieses Skript findet die größten Dateien in einem Verzeichnis.

# Standardwerte
SEARCH_DIR="."  # Standardmäßig das aktuelle Verzeichnis
NUM_FILES=10    # Standardmäßig die Top 10

# Lese Kommandozeilenargumente
if [ -n "$1" ]; then
    SEARCH_DIR=$1
fi
if [ -n "$2" ]; then
    NUM_FILES=$2
fi

# Überprüfe, ob das Verzeichnis existiert
if [ ! -d "$SEARCH_DIR" ]; then
    echo "Fehler: Verzeichnis '$SEARCH_DIR' nicht gefunden."
    exit 1
fi

echo "Suche die $NUM_FILES größten Dateien in '$SEARCH_DIR'..."
echo "-----------------------------------------------------"

# Finde alle Dateien im Verzeichnis (rekursiv),
# ignoriere Fehler (z.B. bei fehlenden Berechtigungen),
# formatiere die Ausgabe mit 'du' für lesbare Größen,
# sortiere nach Größe (numerisch, absteigend),
# und zeige die Top N an.
find "$SEARCH_DIR" -type f -exec du -h {} + 2>/dev/null | sort -rh | head -n "$NUM_FILES"

echo "-----------------------------------------------------"
echo "Suche abgeschlossen."
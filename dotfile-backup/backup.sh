#!/bin/bash

# --- Konfiguration ---
# Liste hier die Dotfiles auf, die du sichern möchtest.
# Gib sie relativ zum Home-Verzeichnis an (ohne ~/).
FILES_TO_BACKUP=(
    ".bashrc"
    ".zshrc"
    ".gitconfig"
    ".vimrc"
    ".config/nvim/init.vim" # Beispiel für eine Datei in einem Unterordner
)

# Zielverzeichnis für das Backup.
# Das Skript erstellt diesen Ordner, falls er nicht existiert.
DEST_DIR="$HOME/dotfile_backup"
# --- Ende der Konfiguration ---


# Erstelle das Zielverzeichnis, falls es nicht existiert
mkdir -p "$DEST_DIR"

echo "Starte Dotfile-Backup nach '$DEST_DIR'..."

# Gehe durch die Liste und kopiere jede Datei
for file in "${FILES_TO_BACKUP[@]}"; do
    SOURCE_FILE="$HOME/$file"
    
    # Prüfe, ob die Quelldatei existiert
    if [ -f "$SOURCE_FILE" ]; then
        # Erstelle die notwendige Ordnerstruktur im Backup-Verzeichnis
        mkdir -p "$(dirname "$DEST_DIR/$file")"
        
        # Kopiere die Datei
        cp "$SOURCE_FILE" "$DEST_DIR/$file"
        echo "  -> '$file' gesichert."
    else
        echo "  -> WARNUNG: '$file' nicht gefunden, wird übersprungen."
    fi
done

echo "Backup erfolgreich abgeschlossen!"
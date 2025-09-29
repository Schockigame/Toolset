import os
import sys
import shutil

# Definiere hier deine Kategorien und die zugehörigen Dateiendungen
FILE_CATEGORIES = {
    "Bilder": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Dokumente": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Musik": [".mp3", ".wav", ".aac"],
    "Archive": [".zip", ".rar", ".tar", ".gz"],
    "Programme": [".exe", ".msi"]
}

def organize_folder(path):
    """
    Organisiert die Dateien im angegebenen Pfad in Unterordner.
    """
    # Überprüfe, ob der Pfad existiert
    if not os.path.isdir(path):
        print(f"Fehler: Der Ordner '{path}' wurde nicht gefunden.")
        return

    print(f"Starte die Organisation des Ordners: {path}")

    # Gehe durch jede Datei im Verzeichnis
    for filename in os.listdir(path):
        # Ignoriere Ordner und versteckte Dateien
        if os.path.isdir(os.path.join(path, filename)) or filename.startswith('.'):
            continue

        # Finde die Dateiendung
        file_extension = os.path.splitext(filename)[1].lower()
        
        # Finde die passende Kategorie
        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                # Erstelle den Kategorie-Ordner, falls er nicht existiert
                category_path = os.path.join(path, category)
                os.makedirs(category_path, exist_ok=True)
                
                # Verschiebe die Datei
                shutil.move(os.path.join(path, filename), os.path.join(category_path, filename))
                print(f"Verschoben: {filename} -> {category}")
                moved = True
                break
        
        if not moved:
            category_path = os.path.join(path, "REST")
            os.makedirs(category_path, exist_ok=True)
            shutil.move(os.path.join(path, filename), os.path.join(category_path, filename))
            print(f"Verschoben: {filename} -> REST")
            moved = True
            
            
    print("Organisation abgeschlossen!")


if __name__ == "__main__":
    # Stelle sicher, dass ein Ordnerpfad als Argument übergeben wurde
    if len(sys.argv) < 2:
        print("Benutzung: python organize.py /pfad/zum/ordner")
    else:
        folder_path = sys.argv[1]
        organize_folder(folder_path)

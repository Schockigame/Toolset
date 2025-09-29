import os
import sys
from PIL import Image

def resize_images(folder_path, max_dimension=1024):
    """
    Verkleinert alle Bilder in einem Ordner auf eine maximale Größe,
    wobei das Seitenverhältnis beibehalten wird.
    """
    # Erstelle einen Ausgabeordner, falls er nicht existiert
    output_folder = os.path.join(folder_path, 'resized')
    os.makedirs(output_folder, exist_ok=True)

    supported_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')

    for filename in os.listdir(folder_path):
        if not filename.lower().endswith(supported_formats):
            continue

        try:
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            
            # Behalte das Seitenverhältnis bei
            width, height = img.size
            if width > max_dimension or height > max_dimension:
                if width > height:
                    new_width = max_dimension
                    new_height = int(new_width * height / width)
                else:
                    new_height = max_dimension
                    new_width = int(new_height * width / height)
                
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

            # Speichere das verkleinerte Bild im 'resized' Ordner
            output_path = os.path.join(output_folder, filename)
            img.save(output_path, optimize=True)
            print(f"Verkleinert: {filename} -> {output_path}")

        except Exception as e:
            print(f"Konnte '{filename}' nicht verarbeiten: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Benutzung: python resize_images.py /pfad/zum/bilder-ordner [maximale_größe]")
        sys.exit(1)
        
    folder = sys.argv[1]
    max_dim = int(sys.argv[2]) if len(sys.argv) > 2 else 1024
    
    if not os.path.isdir(folder):
        print(f"Fehler: Ordner '{folder}' nicht gefunden.")
        sys.exit(1)

    resize_images(folder, max_dim)
    print("\nFertig! Alle Bilder wurden im Unterordner 'resized' gespeichert.")

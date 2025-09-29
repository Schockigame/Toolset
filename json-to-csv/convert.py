import pandas as pd
import sys
import os

def json_to_csv(input_file):
    """
    Konvertiert eine JSON-Datei in eine CSV-Datei.
    Die JSON-Datei muss eine Liste von flachen Objekten sein.
    """
    # Überprüfe Dateiendung
    if not input_file.lower().endswith('.json'):
        print("Fehler: Die Eingabedatei muss eine .json-Datei sein.")
        return

    # Definiere den Ausgabenamen
    output_file = os.path.splitext(input_file)[0] + '.csv'

    try:
        # Lese die JSON-Datei mit Pandas
        df = pd.read_json(input_file)
        
        # Schreibe die Daten in eine CSV-Datei
        df.to_csv(output_file, index=False, encoding='utf-8')
        
        print(f"Erfolgreich konvertiert! '{input_file}' -> '{output_file}'")
    
    except FileNotFoundError:
        print(f"Fehler: Datei '{input_file}' nicht gefunden.")
    except ValueError as e:
        print(f"Fehler beim Verarbeiten der JSON-Datei: {e}")
        print("Stelle sicher, dass die JSON-Datei eine Liste von Objekten ist.")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Benutzung: python convert.py <dateiname.json>")
        sys.exit(1)
        
    json_file = sys.argv[1]
    json_to_csv(json_file)

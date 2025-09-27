import requests

URL_FILE = 'urls.txt'

def check_urls():
    """
    Liest URLs aus einer Datei und überprüft ihren Status.
    """
    try:
        with open(URL_FILE, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Fehler: Die Datei '{URL_FILE}' wurde nicht gefunden.")
        return

    print(f"Überprüfe {len(urls)} URLs...")
    
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"✅ [200 OK] {url}")
            else:
                print(f"⚠️ [{response.status_code}] {url}")
        except requests.ConnectionError:
            print(f"❌ [FEHLER] {url} - Verbindung fehlgeschlagen.")
        except requests.Timeout:
            print(f"❌ [FEHLER] {url} - Timeout.")
        except requests.RequestException as e:
            print(f"❌ [FEHLER] {url} - {e}")

if __name__ == "__main__":
    check_urls()
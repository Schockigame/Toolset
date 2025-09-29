import http.server
import socketserver
import sys
s
# Standardport, falls keiner angegeben wird
PORT = 8000

# Wähle den Port aus den Kommandozeilenargumenten, wenn vorhanden
if len(sys.argv) > 1:
    try:
        PORT = int(sys.argv[1])
    except ValueError:
        print("Fehler: Bitte eine gültige Portnummer angeben.")
        sys.exit(1)

# Handler, der die Anfragen bearbeitet
Handler = http.server.SimpleHTTPRequestHandler

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Lokaler Webserver gestartet auf http://localhost:{PORT}")
        print("Drücke STRG+C, um den Server zu beenden.")
        # Starte den Server und warte auf Anfragen
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer wird heruntergefahren.")
    httpd.shutdown()
except OSError as e:
    print(f"Fehler: Port {PORT} ist möglicherweise bereits in Verwendung. {e}")

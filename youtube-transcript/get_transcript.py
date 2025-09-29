import sys
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    """
    Extrahiert die Video-ID aus einer YouTube-URL.
    Funktioniert für Standard- und Kurz-URLs (youtu.be) und entfernt störende Zeichen.
    """
    # Bereinige die URL von versehentlichen Markdown-Resten, Leerzeichen und Anführungszeichen
    url = url.strip("[]()").strip().strip('"')

    if "v=" in url:
        # Extrahiert ID und verwirft alles danach (&, #, etc.)
        return url.split("v=")[1].split('&')[0].split('#')[0]
    elif "youtu.be/" in url:
        # Extrahiert ID und verwirft alles danach (/, ?, & etc.)
        return url.split("youtu.be/")[1].split('/')[0].split('?')[0].split('&')[0]
    return None

def download_transcript(video_id):
    """
    Lädt das Transkript für eine gegebene Video-ID herunter.
    
    1. Versucht, Deutsch/Englisch zu finden.
    2. Fällt auf Übersetzung nach Deutsch zurück, wenn nur eine andere Sprache verfügbar ist.
    """
    try:
        print(f"Versuche, Transkript für Video-ID '{video_id}' zu laden...")

        # Instanziieren der YouTubeTranscriptApi
        ytt_api = YouTubeTranscriptApi()
        
        # Holt die Liste aller verfügbaren Transkripte
        transcripts = ytt_api.list(video_id)
        
        transcript = None
        
        # 1. Versuche, direkt ein deutsches oder englisches Transkript zu finden
        try:
            # Sucht in der Prioritätsreihenfolge ['de', 'en']
            transcript = transcripts.find_transcript(['de', 'en'])
            print(f"Ursprüngliches Transkript in '{transcript.language}' gefunden.")
        except Exception:
            # 2. Kein direktes deutsches/englisches Transkript gefunden, suche nach einem beliebigen Transkript
            try:
                # Finde das beste verfügbare Transkript (meistens die Originalsprache)
                transcript = transcripts.find_transcript([]) 
                
                if transcript and transcript.is_translatable:
                    print(f"Ursprüngliches Transkript in '{transcript.language}' gefunden. Versuche deutsche Übersetzung...")
                    
                    # Übersetze das gefundene Transkript nach Deutsch
                    transcript = transcript.translate('de')
                    print("Erfolgreich nach Deutsch übersetzt.")
                    
                elif transcript and not transcript.is_translatable:
                    print(f"⚠️ Transkript in '{transcript.language}' gefunden, aber nicht übersetzbar. Keine Aktion möglich.")
                    transcript = None # Setze auf None, da keine DE-Version verfügbar
                else:
                    # Immer noch kein Transkript gefunden
                    pass

            except Exception as e:
                print(f"Fehler bei Suche/Übersetzung eines verfügbaren Transkripts.")
                # print(f"   Details: {e}") # Kann bei erfolgreicher Code-Basis weggelassen werden
                transcript = None
        
        if not transcript:
            print("❌ Fehler: Kein Transkript in DE oder EN verfügbar, auch keine Basis für Übersetzung.")
            return

        # Holt den eigentlichen Text und kombiniert ihn zu einem String
        # KORRIGIERT: Zugriff auf den Text über 'item.text' statt 'item['text']'
        full_transcript = " ".join([item.text for item in transcript.fetch()])

        # Speichere das Transkript in einer Datei
        filename = f"{video_id}_transcript.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(full_transcript)
            
        print(f"Transkript erfolgreich in '{filename}' gespeichert.")
        
    except Exception as e:
        print(f"Schwerwiegender Fehler: Konnte kein Transkript für dieses Video finden oder laden.")
        # Dieser Block fängt jetzt nur noch Fehler ab, die nicht von der fehlenden Sprache stammen (z.B. IP-Block oder fehlerhafte Video-ID)
        print(f"   Grund: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Benutzung: python get_transcript.py <YouTube_URL>")
        sys.exit(1)
        
    video_url = sys.argv[1]
    video_id = get_video_id(video_url)
    
    if not video_id:
        print("Fehler: Ungültige YouTube-URL.")
        sys.exit(1)
        
    download_transcript(video_id)

import sys
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    """
    Extrahiert die Video-ID aus einer YouTube-URL.
    Funktioniert für Standard- und Kurz-URLs (youtu.be).
    """
    if "v=" in url:
        return url.split("v=")[1].split('&')[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1]
    return None

def download_transcript(video_id):
    """
    Lädt das Transkript für eine gegebene Video-ID herunter und speichert es.
    """
    try:
        print(f"Versuche, Transkript für Video-ID '{video_id}' zu laden...")
        # Holt das Transkript als Liste von Dictionaries
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['de', 'en'])
        
        # Formatiere den Text in einen einzigen String
        full_transcript = " ".join([item['text'] for item in transcript_list])
        
        # Speichere das Transkript in einer Datei
        filename = f"{video_id}_transcript.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(full_transcript)
            
        print(f"✅ Transkript erfolgreich in '{filename}' gespeichert.")
        
    except Exception as e:
        print(f"❌ Fehler: Konnte kein Transkript für dieses Video finden oder laden.")
        print(f"   Grund: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Benutzung: python get_transcript.py \"<YouTube_URL>\"")
        sys.exit(1)
        
    video_url = sys.argv[1]
    video_id = get_video_id(video_url)
    
    if not video_id:
        print("Fehler: Ungültige YouTube-URL.")
        sys.exit(1)
        
    download_transcript(video_id)
import markdown
import sys

def convert_markdown_to_html(input_file, output_file):
    """
    Liest eine Markdown-Datei und konvertiert sie in eine HTML-Datei.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            md_text = f.read()
    except FileNotFoundError:
        print(f"Fehler: Die Eingabedatei '{input_file}' wurde nicht gefunden.")
        return

    # Konvertiere Markdown zu HTML
    html = markdown.markdown(md_text)

    # Erstelle eine vollständige HTML-Struktur mit einfachem Styling
    html_template = f"""
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-g">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{input_file}</title>
        <style>
            body {{ font-family: sans-serif; line-height: 1.6; max-width: 800px; margin: 40px auto; padding: 0 20px; }}
            code {{ background-color: #f4f4f4; padding: 2px 4px; border-radius: 4px; }}
            pre {{ background-color: #f4f4f4; padding: 1em; overflow-x: auto; }}
        </style>
    </head>
    <body>
        {html}
    </body>
    </html>
    """
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_template)
        print(f"Erfolgreich konvertiert: '{input_file}' -> '{output_file}'")
    except Exception as e:
        print(f"Fehler beim Schreiben der HTML-Datei: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Benutzung: python convert.py beispiel.md")
        sys.exit(1)

    input_md_file = sys.argv[1]
    if not input_md_file.lower().endswith('.md'):
        print("Fehler: Die Eingabedatei muss eine .md-Datei sein.")
        sys.exit(1)

    output_html_file = input_md_file[:-3] + '.html'
    convert_markdown_to_html(input_md_file, output_html_file)

#!/usr/bin/env python3
# Hockey DJ - Lokal webserver (Python)
# Kjør med: python3 server.py
# Ingen ekstra pakker nødvendig — bruker kun innebygde Python-biblioteker

import http.server
import socketserver
import webbrowser
import threading
import os
import sys

PORT = 8080
HOST = "localhost"
URL  = f"http://{HOST}:{PORT}"

# Bytt til mappen der denne filen ligger
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    """Serve filer, og fall tilbake til index.html for alle ukjente paths
    (slik at Spotify redirect til / fungerer korrekt)."""

    def do_GET(self):
        # Strip query-string og fragment
        path = self.path.split("?")[0].split("#")[0]
        if path == "/" or not os.path.exists("." + path):
            self.path = "/index.html"
        return super().do_GET()

    def log_message(self, format, *args):
        # Stilig logg i terminalen
        print(f"  → {args[0]} {args[1]}")

def open_browser():
    webbrowser.open(URL)

print()
print("  🏒  Hockey DJ er klar!")
print("  ──────────────────────────────────────")
print(f"  Åpne:          {URL}")
print(f"  Redirect URI:  {URL}/")
print("  ──────────────────────────────────────")
print("  Husk å legge inn Redirect URI i")
print("  Spotify Developer Dashboard!")
print()
print("  Trykk Ctrl+C for å stoppe serveren.")
print()

# Åpne nettleseren etter 0.5 sekunder (server må starte først)
threading.Timer(0.5, open_browser).start()

try:
    with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
        httpd.serve_forever()
except OSError as e:
    if "Address already in use" in str(e):
        print(f"\n  ❌  Port {PORT} er allerede i bruk.")
        print(f"  Prøv å åpne {URL} direkte i nettleseren,")
        print("  eller stopp den andre prosessen og prøv igjen.\n")
    else:
        print(f"\n  ❌  Feil: {e}\n")
    sys.exit(1)
except KeyboardInterrupt:
    print("\n\n  Hockey DJ stoppet. Ha en god kamp! 🏒\n")

# 🏒 Hockey DJ

Spotify DJ-app for hockeykamper. Søk og importer låter og playlists, sett start/stopp-punkt per sang, og kategoriser spor (mål, powerplay, intro, timeout osv.).

---

## Kom i gang

### 1. Sjekk at Python er installert
Åpne Terminal (Mac) eller Ledetekst (Windows) og kjør:
```
python3 --version
```
Du skal se noe som `Python 3.x.x`. Python er forhåndsinstallert på de fleste Mac og bedriftsmaskiner.

### 2. Start appen

**Mac / Linux:**
```bash
bash start.sh
```
Eller høyreklikk `start.sh` → Åpne med Terminal.

**Windows:**
Dobbeltklikk `start.bat`

Appen åpner seg automatisk på `http://localhost:8080` 🎉

---

## Spotify-oppsett (én gang)

1. Gå til **https://developer.spotify.com/dashboard**
2. Logg inn og klikk **"Create app"**
3. Fyll inn:
   - App name: `Hockey DJ` (valgfritt)
   - Redirect URI: `http://localhost:8080/`  ← viktig!
4. Kopier **Client ID**
5. Lim inn Client ID i appen når du logger inn

---

## Funksjoner

- 🔍 Søk etter låter og playlists via Spotify
- 📋 Importer hele playlists via URL
- ✂️ Sett start- og stoppunkt per låt
- 🏷️ Kategorier: Mål, Powerplay, Intro, Pump, Timeout
- 🔀 Drag & drop rekkefølge i køen
- ⏭ Autoplay til neste låt
- 👤 Brukerprofilvisning i headeren

---

## Filer

```
hockey-dj/
├── index.html    ← selve appen
├── server.py     ← lokal webserver (Python, ingen ekstra pakker)
├── start.sh      ← oppstart Mac/Linux
├── start.bat     ← oppstart Windows
└── README.md     ← denne filen
```

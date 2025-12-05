# 🎄 LAUFADVENTSKALENDER 🏃‍♂️

Ein interaktiver Adventskalender für Läufer und Sportler mit Pixel-Art Christmas-Design!

## 🎯 WAS IST DAS?

Der Laufadventskalender ist eine Webanwendung, die es dir ermöglicht, deine sportlichen Aktivitäten im Dezember zu tracken. Jedes Adventstürchen repräsentiert eine bestimmte Kilometerzahl, die du laufen oder radeln kannst.

## 🚀 FUNKTIONEN

### 🏠 Startseite
- Persönlichen Namen eingeben
- Direkter Zugang zum eigenen Kalender
- Erklärung der Spielregeln
- Navigation zur Übersicht

**Screenshot:**
```
[📸 HIER STARTSEITEN-SCREENSHOT EINFÜGEN]
```

### 👤 Persönliche Kalenderseite
- 24 interaktive Adventstürchen (1-24)
- Jedes Türchen = seine Tagesnummer als Kilometer
- Christmas-Emojis für jeden Tag
- Echtzeit-Kilometerzähler
- Klick zum Aktivieren/Deaktivieren
- Daten werden automatisch gespeichert

**Screenshot:**
```
[📸 HIER PERSÖNLICHE KALENDER-SCREENSHOT EINFÜGEN]
```

### 📊 Übersichtsseite
- Alle Teilnehmer auf einen Blick
- Gesamtkilometer aller Nutzer
- Fortschrittstabelle für jeden Teilnehmer
- Klickbare Nutzerlinks zu den individuellen Kalendern

**Screenshot:**
```
[📸 HIER ÜBERSICHTS-SCREENSHOT EINFÜGEN]
```

## 🎮 SPIELREGELN

### 📅 Zeitraum
- **1. bis 24. Dezember**: Jeden Tag eine Strecke laufen oder radeln

### 🔄 Reihenfolge
- **Frei wählbar**: Du entscheidest, welche Tage du wann machst

### ⚖️ Umrechnung
- **250m Schwimmen** = 1km Laufen
- **5km Radfahren** = 1km Laufen

### 🎯 Kilometer
- **Jedes Türchen = seine Tagesnummer als Kilometer**
  - Türchen 1 = 1km
  - Türchen 16 = 16km
  - Türchen 24 = 24km

## 🛠️ TECHNISCHE DETAILS

### 🏗️ Architektur
- **Backend**: Python Flask mit SQLite-Datenbank
- **Frontend**: HTML5 mit Bulma CSS Framework
- **Design**: Custom Pixel-Art Christmas Theme
- **Datenbank**: SQLite für Benutzerdaten und Button-States

### 📁 Projektstruktur
```
📁 laufadvent/
├── 📁 backend/
│   ├── 🐍 app.py              # Flask-App mit API-Endpunkten
│   ├── 🐍 database.py         # Datenbank-Initialisierung
│   ├── 🐍 test_app.py         # Unit-Tests
│   ├── 📄 requirements.txt    # Python-Abhängigkeiten
│   └── 📁 instance/
│       └── 💾 database.db     # SQLite-Datenbank
├── 📁 static/
│   └── 📁 css/
│       └── 🎨 pixel-art.css   # Pixel-Art Christmas Styles
├── 📁 templates/
│   ├── 📄 index.html          # Startseite
│   ├── 📄 user.html           # Persönlicher Kalender
│   └── 📄 overview.html       # Übersichtsseite
└── 🚀 start-servers.sh        # Start-Script
```

### 🔧 API-Endpunkte

#### `GET /api/<username>`
- Lädt Benutzerdaten und Button-States
- Erstellt neuen Benutzer falls nicht vorhanden

#### `POST /api/<username>`
- Aktualisiert Button-Status
- `{"button_number": 16, "is_on": true}`

#### `DELETE /api/<username>`
- Löscht Benutzer und alle zugehörigen Daten

#### `GET /api/overview`
- Lädt Übersicht aller Teilnehmer
- Berechnet Gesamtkilometer

### 🎨 Design-Features
- **Pixel-Art Ästhetik** mit 8-Bit Christmas-Theme
- **Animierter Schneefall** als Hintergrundeffekt
- **Responsive Design** für Mobile und Desktop
- **Interaktive Buttons** mit Hover- und Click-Effekten
- **Christmas-Emojis** für jeden Tag
- **Custom Scrollbar** für Übersichtstabelle


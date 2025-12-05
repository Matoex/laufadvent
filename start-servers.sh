#!/bin/bash

# Laufadventskalender - Startskript für Backend und Frontend
# Dieses Skript startet beide Server und stoppt sie bei Ctrl+C

# Funktion zum Aufräumen beim Beenden
cleanup() {
    echo -e "\n🛑 Stoppe Server..."
    
    # Backend stoppen
    if [ ! -z "$BACKEND_PID" ]; then
        echo "Stoppe Backend (PID: $BACKEND_PID)"
        kill $BACKEND_PID 2>/dev/null
    fi
    
    
    
    # Warte auf Beendigung
    wait $BACKEND_PID 2>/dev/null
    wait $FRONTEND_PID 2>/dev/null
    
    echo "✅ Alle Server gestoppt"
    exit 0
}

# Signalhandler für Ctrl+C
trap cleanup SIGINT SIGTERM

echo "🎄 Starte Laufadventskalender Server..."
echo "=================================="

# Backend starten
echo "🔧 Starte Backend Server..."
cd backend
python3 app.py &
BACKEND_PID=$!
echo "Backend gestartet (PID: $BACKEND_PID) auf http://localhost:5000"

# Kurze Pause für Backend-Start
sleep 2

# Prüfen ob Backend läuft
if ! kill -0 $BACKEND_PID 2>/dev/null; then
    echo "❌ Backend konnte nicht gestartet werden!"
    exit 1
fi

echo ""
echo "🚀 Server ist bereit!"
echo "===================="
echo "Backend:  http://localhost:5000"
echo ""
echo "Drücke Ctrl+C um Server zu stoppen"
echo ""

# Warte auf den Hintergrundprozess
wait $BACKEND_PID
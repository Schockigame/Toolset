#!/bin/bash

# Farben für die Ausgabe
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# --- Systeminformationen ---
HOSTNAME=$(hostname)
DATE=$(date "+%Y-%m-%d %H:%M:%S")

# --- CPU-Auslastung ---
# Liest die Durchschnittslast der letzten Minute
CPU_LOAD=$(uptime | awk -F'load average: ' '{print $2}' | cut -d, -f1)

# --- RAM-Auslastung ---
# Liest den Gesamtspeicher und den genutzten Speicher aus /proc/meminfo
# Funktioniert zuverlässig auf den meisten Linux-Systemen
TOTAL_MEM=$(grep MemTotal /proc/meminfo | awk '{print $2}')
FREE_MEM=$(grep MemAvailable /proc/meminfo | awk '{print $2}')
USED_MEM=$((TOTAL_MEM - FREE_MEM))
MEM_USAGE_PERCENT=$(awk "BEGIN {printf \"%.2f\", $USED_MEM/$TOTAL_MEM*100}")

# --- Festplatten-Auslastung (Root-Verzeichnis) ---
DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')


# --- Ausgabe ---
echo -e "==========================================="
echo -e "    SYSTEM HEALTH REPORT für ${GREEN}$HOSTNAME${NC}"
echo -e "    ${YELLOW}$DATE${NC}"
echo -e "==========================================="
echo ""
echo -e "📊 ${GREEN}CPU-LAST (1 min):${NC}  $CPU_LOAD"
echo -e "🧠 ${GREEN}RAM-NUTZUNG:${NC}       $MEM_USAGE_PERCENT %"
echo -e "💾 ${GREEN}FESTPLATTE (/):${NC}  $DISK_USAGE % belegt"
echo ""
echo -e "==========================================="
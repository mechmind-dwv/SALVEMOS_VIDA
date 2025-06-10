#!/bin/bash
# emergency_protocol.sh

# 1. Monitoreo constante
while true; do
    DATA=$(python3 monitoring_system.py)
    TEMP=$(echo $DATA | jq '.oceanic.water_temp')
    QUAKES=$(echo $DATA | jq '.tectonic.last_quake.magnitude')
    
    # 2. Umbrales de alerta
    if (( $(echo "$TEMP > 28" | bc -l) )); then
        echo "ALERTA: Temperatura anormal en Golfo de Cádiz"
        python3 send_alert.py --type ocean --value $TEMP
    fi

    if (( $(echo "$QUAKES > 4.5" | bc -l) )); then
        echo "ALERTA SÍSMICA: Terremoto de magnitud $QUAKES"
        python3 activate_sirens.py --zone all
    fi

    sleep 300  # Chequeo cada 5 minutos
done

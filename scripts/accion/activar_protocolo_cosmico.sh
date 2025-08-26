#!/bin/bash
# scripts/accion/activar_protocolo_cosmico.sh

echo "🌌 ACTIVANDO PROTOCOLO CÓSMICO - $1"
echo "⏰ Timestamp: $(date)"
echo "📍 GPS: 36.7360° N, 6.4376° W"

case $1 in
    "CÓSMICA")
        echo "☀️ ALERTA CÓSMICA: Tormenta geomagnética detectada!"
        echo "📡 Aumento riesgo sísmico y de tsunamis"
        python -m scripts.alertas.telegram_bot "🌌 ALERTA CÓSMICA: Actividad solar extrema. Monitorizar sismos."
        ;;
    "S1")
        echo "⚠️ ALERTA RADIACIÓN S1: Lluvia de protones"
        echo "🚨 Riesgo para astronautas y aviación"
        python -m scripts.alertas.telegram_bot "☢️ ALERTA RADIACIÓN S1: Evitar altitudes elevadas."
        ;;
    "G4")
        echo "⚡ ALERTA GEOMAGNÉTICA G4: Tormenta severa"
        echo "🔌 Posibles apagones e interferencias"
        python -m scripts.alertas.telegram_bot "⚡ ALERTA GEOMAGNÉTICA G4: Preparar sistemas de backup."
        ;;
    "TEST")
        echo "🧪 PRUEBA SISTEMA CÓSMICO"
        python -m scripts.alertas.telegram_bot "🌠 PRUEBA ALERTA CÓSMICA: Sistema operativo."
        ;;
    *)
        echo "❌ Alerta cósmica no reconocida: $1"
        exit 1
        ;;
esac

echo "📞 Contacto emergencia: +34 644 17 85 10"
echo "🌐 Centro de Operaciones: Avda. del Mar, 12"

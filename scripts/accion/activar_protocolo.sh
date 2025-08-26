#!/bin/bash
# scripts/accion/activar_protocolo.sh

echo "🚨 ACTIVANDO PROTOCOLO DE EMERGENCIA CHIPIONA - $1"
echo "⏰ Timestamp: $(date)"
echo "📍 GPS: 36.7360° N, 6.4376° W"

case $1 in
    "SÍSMICA")
        echo "📢 ALERTA SÍSMICA: Evacuar zonas costeras!"
        python -m scripts.alertas.telegram_bot "TERREMOTO DETECTADO. Evacuar zona costera inmediatamente. Punto de encuentro: Plaza Andalucía"
        python -m scripts.alertas.email_emergencia "Alerta sísmica activada. Magnitud crítica detectada."
        ;;
    "TÉRMICA")
        echo "🌡️ ALERTA TÉRMICA: Temperatura del agua crítica!"
        python -m scripts.alertas.telegram_bot "ALERTA TÉRMICA: Temperatura del agua anormal. Posible riesgo."
        ;;
    "TEST")
        echo "🧪 MODO PRUEBA: Probando sistema..."
        python -m scripts.alertas.telegram_bot "✅ SISTEMA DE PRUEBA: Alertas funcionando correctamente"
        echo "✅ Prueba completada"
        ;;
    *)
        echo "❌ Alerta no reconocida: $1"
        echo "💡 Usar: SÍSMICA, TÉRMICA o TEST"
        exit 1
        ;;
esac

echo "📞 Contacto emergencia: +34 644 17 85 10"
echo "🌐 Centro de Operaciones: Avda. del Mar, 12"

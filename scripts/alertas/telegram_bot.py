#!/usr/bin/env python3
# scripts/alertas/telegram_bot.py

import requests
import sys
from scripts.config.tokens import token_manager
from datetime import datetime

def enviar_alerta_telegram(mensaje):
    """Envía alerta por Telegram (GRATIS)"""
    bot_token = token_manager.get_token('telegram', 'bot_token')
    chat_id = token_manager.get_token('telegram', 'chat_id')
    
    if not bot_token or not chat_id:
        print("❌ Telegram no configurado correctamente")
        return False
    
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': f"🚨 ALERTA OFICIAL CHIPIONA\n📋 Tipo: {mensaje}\n⏰ Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n📍 GPS: 36.7360° N, 6.4376° W\n📞 Emergencias: +34 644 17 85 10",
        }
        
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("✅ Alerta enviada por Telegram")
            return True
        else:
            print(f"❌ Error Telegram: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error enviando a Telegram: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        mensaje = " ".join(sys.argv[1:])
        enviar_alerta_telegram(mensaje)
    else:
        print("💡 Uso: python -m scripts.alertas.telegram_bot 'mensaje'")

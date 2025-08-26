#!/usr/bin/env python3
# scripts/alertas/sms_emergencia.py

import sys
from scripts.config.tokens import token_manager

def enviar_sms(mensaje):
    """Envía SMS de emergencia usando Twilio"""
    sid = token_manager.get_token('twilio', 'sid')
    auth_token = token_manager.get_token('twilio', 'auth_token')
    from_phone = token_manager.get_token('twilio', 'phone')
    
    if not all([sid, auth_token, from_phone]):
        print("❌ Twilio no configurado. Ejecuta: python -m scripts.config.setup_tokens")
        return False
    
    try:
        # Simulación - Aquí iría el código real de Twilio
        print(f"📲 ENVIANDO SMS: {mensaje}")
        print(f"   From: {from_phone}")
        print(f"   Twilio SID: {sid}")
        return True
    except Exception as e:
        print(f"❌ Error enviando SMS: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        mensaje = sys.argv[1]
        enviar_sms(mensaje)
    else:
        print("💡 Uso: python -m scripts.alertas.sms_emergencia 'mensaje'")

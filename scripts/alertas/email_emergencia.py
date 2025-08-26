#!/usr/bin/env python3
# scripts/alertas/email_emergencia.py

import smtplib
import sys
from email.mime.text import MIMEText
from scripts.config.tokens import token_manager

def enviar_email_emergencia(mensaje, asunto="🚨 ALERTA CHIPIONA"):
    """Envía alerta por email (Gmail gratis)"""
    try:
        # Configuración simple para Gmail
        email = "tu.email@gmail.com"  # Cambiar esto
        password = "tu_password"      # Cambiar esto
        
        msg = MIMEText(mensaje)
        msg['Subject'] = asunto
        msg['From'] = email
        msg['To'] = "emergencias@chipiona.es"  # Email del ayuntamiento
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(email, password)
            server.send_message(msg)
        
        print("✅ Email de alerta enviado")
        return True
        
    except Exception as e:
        print(f"❌ Error enviando email: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        mensaje = " ".join(sys.argv[1:])
        enviar_email_emergencia(mensaje)
    else:
        print("💡 Uso: python -m scripts.alertas.email_emergencia 'mensaje'")

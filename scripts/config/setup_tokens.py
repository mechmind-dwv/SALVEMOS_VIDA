#!/usr/bin/env python3
# scripts/config/setup_tokens.py

from .tokens import token_manager


def setup_interactive():
    """Configuración interactiva de tokens"""
    print("🎯 CONFIGURACIÓN DE TOKENS - SALVEMOS VIDAS")
    print("=" * 50)

    # Twilio (SMS)
    print("\n📱 CONFIGURACIÓN TWILIO (SMS):")
    sid = input("Twilio SID (deja vacío si no tienes): ").strip()
    if sid:
        auth_token = input("Twilio Auth Token: ").strip()
        phone = input("Número Twilio: ").strip()
        token_manager.set_token("twilio", "sid", sid)
        token_manager.set_token("twilio", "auth_token", auth_token)
        token_manager.set_token("twilio", "phone", phone)

    # Telegram
    print("\n📢 CONFIGURACIÓN TELEGRAM:")
    bot_token = input("Token del bot de Telegram: ").strip()
    if bot_token:
        chat_id = input("Chat ID: ").strip()
        token_manager.set_token("telegram", "bot_token", bot_token)
        token_manager.set_token("telegram", "chat_id", chat_id)

    print("\n✅ Configuración completada!")
    print(f"📁 Config guardada en: {token_manager.config_file}")


if __name__ == "__main__":
    setup_interactive()

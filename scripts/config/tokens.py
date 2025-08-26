#!/usr/bin/env python3
# scripts/config/tokens.py

import os
import json
from pathlib import Path

class TokenManager:
    def __init__(self):
        self.config_dir = Path.home() / ".salvemos_vida"
        self.config_file = self.config_dir / "tokens.json"
        self.tokens = self._load_tokens()
    
    def _load_tokens(self):
        """Carga los tokens desde el archivo de configuración"""
        if not self.config_file.exists():
            return {
                'twilio': {'sid': '', 'auth_token': '', 'phone': ''},
                'telegram': {'bot_token': '', 'chat_id': ''},
                'whatsapp': {'api_key': ''},
                'twitter': {'api_key': '', 'api_secret': ''}
            }
        
        with open(self.config_file, 'r') as f:
            return json.load(f)
    
    def save_tokens(self):
        """Guarda los tokens en el archivo de configuración"""
        self.config_dir.mkdir(exist_ok=True)
        with open(self.config_file, 'w') as f:
            json.dump(self.tokens, f, indent=4)
    
    def set_token(self, service, key, value):
        """Establece un token específico"""
        if service not in self.tokens:
            self.tokens[service] = {}
        self.tokens[service][key] = value
        self.save_tokens()
        print(f"✅ Token {service}.{key} configurado correctamente")
    
    def get_token(self, service, key):
        """Obtiene un token específico"""
        return self.tokens.get(service, {}).get(key, None)

# Instancia global
token_manager = TokenManager()

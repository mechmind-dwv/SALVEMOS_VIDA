#!/usr/bin/env python3
# scripts/monitoreo/service_24_7.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import time
import logging
from scripts.monitoreo.alert_system import main as monitor_main

# Configurar logging
logging.basicConfig(
    filename='logs/sistema_alertas.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_service():
    """Ejecuta el sistema 24/7 con reinicios automáticos"""
    print("🔧 Iniciando servicio 24/7 de alertas...")
    logging.info("Sistema de alertas iniciado")

    while True:
        try:
            monitor_main()
        except Exception as e:
            logging.error(f"Error en sistema: {e}")
            print(f"⚠️ Error: {e}. Reiniciando en 30 segundos...")
            time.sleep(30)

if __name__ == "__main__":
    run_service()

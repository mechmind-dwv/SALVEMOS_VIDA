#!/usr/bin/env python3
# scripts/monitoreo/alert_system.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import time
import subprocess
from scripts.monitoreo.data_integrator import DataFetcher

class AlertManager:
    UMBRALES = {
        'sismo': 4.5,  # Escala Richter
        'temp_agua': 28.0,  # °C
        'nivel_marea': 2.5  # metros
    }

    def check_alertas(self, data):
        """Verifica si se superan los umbrales de alerta"""
        alertas = []
        
        # ALERTA SÍSMICA (magnitud + proximidad)
        if data['sismos']['max_magnitud'] > self.UMBRALES['sismo']:
            if data['sismos']['ultimo_sismo'] and data['sismos']['ultimo_sismo']['distancia_km'] < 100:
                alertas.append('SÍSMICA')
        
        # ALERTA TÉRMICA (temperatura del agua)
        if data['temperatura']['valor'] > self.UMBRALES['temp_agua']:
            alertas.append('TÉRMICA')
            
        # ALERTA DE MAREA (nivel anormal)
        if data['mareas']['nivel_actual'] > self.UMBRALES['nivel_marea']:
            alertas.append('DE MAREA')
            
        return alertas

def main():
    """Sistema principal de monitoreo"""
    print("🚀 Iniciando Sistema de Alertas de Chipiona...")
    print("📡 Monitoreando datos en tiempo real...")
    
    fetcher = DataFetcher()
    manager = AlertManager()
    
    try:
        while True:
            # Obtener datos
            datos = fetcher.fetch_data()
            
            # Verificar alertas
            alertas_activas = manager.check_alertas(datos)
            
            if alertas_activas:
                print(f"🚨 ALERTA ACTIVADA: {', '.join(alertas_activas)}")
                
                # Enviar alerta por Telegram
                try:
                    from scripts.alertas.telegram_bot import enviar_alerta_telegram
                    mensaje = f"ALERTA {', '.join(alertas_activas)} ACTIVADA"
                    enviar_alerta_telegram(mensaje)
                    print("✅ Alerta enviada por Telegram")
                except Exception as e:
                    print(f"❌ Error enviando alerta: {e}")
                
                # Activar protocolo de emergencia
                for alerta in alertas_activas:
                    try:
                        subprocess.run(["./scripts/accion/activar_protocolo.sh", alerta])
                    except Exception as e:
                        print(f"❌ Error activando protocolo {alerta}: {e}")
            else:
                print("✅ Todo normal - Sin alertas")
            
            # Esperar 60 segundos entre chequeos
            time.sleep(60)
            
    except KeyboardInterrupt:
        print("\n🛑 Sistema de alertas detenido manualmente")
    except Exception as e:
        print(f"❌ Error crítico: {str(e)}")

if __name__ == "__main__":
    main()

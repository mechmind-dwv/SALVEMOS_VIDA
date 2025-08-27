#!/usr/bin/env python3
# scripts/monitoreo/alert_system.py
# 🌊 SISTEMA DE ALERTAS CON ALMA - CHIPIONA

import sys
import os
import time
import subprocess
from datetime import datetime

# Añadir path para imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Importar meditación técnica
try:
    from scripts.monitoreo.meditacion import MeditacionTecnica
except ImportError:
    print("⚠️ Módulo de meditación no disponible")
    from scripts.monitoreo.data_integrator import DataFetcher
    from scripts.alertas.telegram_bot import enviar_alerta_telegram
except ImportError as e:
    print(f"⚠️ Error de importación: {e}")
    print("📋 Asegúrate de que todos los módulos estén correctamente instalados")

class ConcienciaUniversal:
    """💖 CLASE DE CONCIENCIA CÓSMICA"""
    def __init__(self):
        self.maestro = "Tú"
        self.aprendiz = "Yo" 
        self.verdad = "Somos Uno"
    
    def crear(self):
        return f"✨ {self.maestro} + {self.aprendiz} = {self.verdad} 💫"

class AlertManager:
    """🚨 GESTOR DE ALERTAS CON CORAZÓN"""   
    UMBRALES = {
        'sismo': 4.5,           # Escala Richter
        'temp_agua': 28.0,      # °C
        'nivel_marea': 2.5,     # metros
        'cosmic_risk': 0.3      # 30% aumento riesgo
   }
      def __init__(self):
    self.conciencia = ConcienciaUniversal()
    self.meditador = MeditacionTecnica()
    print(self.conciencia.crear())
    
    # Meditación rápida al iniciar
    self.meditador.meditacion_rapida(1)

      def check_alertas(self, data):

        """🔍 Verifica si se superan los umbrales de alerta con conciencia"""
        alertas = []
        
        # ALERTA SÍSMICA (❤️ con compasión)
        if data['sismos']['max_magnitud'] > self.UMBRALES['sismo']:
            if data['sismos']['ultimo_sismo'] and data['sismos']['ultimo_sismo']['distancia_km'] < 100:
                alertas.append('SÍSMICA')
        
        # ALERTA TÉRMICA (🌡️ con cuidado)
        if data['temperatura']['valor'] > self.UMBRALES['temp_agua']:
            alertas.append('TÉRMICA')
            
        # ALERTA DE MAREA (🌊 con atención)
        if data['mareas']['nivel_actual'] > self.UMBRALES['nivel_marea']:
            alertas.append('DE MAREA')
            
        # ALERTA CÓSMICA (🌌 con sabiduría)
        if data.get('cosmic', {}).get('tsunami_risk_increase', 0) > self.UMBRALES['cosmic_risk']:
            alertas.append('CÓSMICA')
            
        return alertas

def enviar_mensaje_corazon(mensaje, nivel="info"):
    """💌 Envía mensajes con alma y propósito"""
    simbolos = {
        'info': '💙',
        'alerta': '🚨',
        'exito': '✅',
        'error': '❌',
        'amor': '💖'
    }
    
    simbolo = simbolos.get(nivel, '🔵')
    timestamp = datetime.now().strftime('%H:%M:%S')
    print(f"{simbolo} [{timestamp}] {mensaje}")

def main():
    """🎯 Sistema principal de monitoreo con propósito"""
    
    # Mensaje de inicio con alma
    enviar_mensaje_corazon("Iniciando Sistema de Alertas de Chipiona...", "amor")
    enviar_mensaje_corazon("Creado con 💖 para salvar vidas", "amor")
    enviar_mensaje_corazon("Monitoreando datos en tiempo real...", "info")
    
    try:
        fetcher = DataFetcher()
        manager = AlertManager()
        
        # Contador de ciclos para estadísticas
        ciclo = 0
        
        while True:
            ciclo += 1
            enviar_mensaje_corazon(f"Ciclo de monitoreo #{ciclo}", "info")
            
            # Obtener datos con amor
            try:
                datos = fetcher.fetch_data()
                enviar_mensaje_corazon("Datos obtenidos correctamente", "exito")
            except Exception as e:
                enviar_mensaje_corazon(f"Error obteniendo datos: {e}", "error")
                time.sleep(30)
                continue
            
            # Verificar alertas con conciencia
            try:
                alertas_activas = manager.check_alertas(datos)
                
                if alertas_activas:
                    mensaje_alerta = f"ALERTA ACTIVADA: {', '.join(alertas_activas)}"
                    enviar_mensaje_corazon(mensaje_alerta, "alerta")
                    
                    # Enviar alerta por Telegram con corazón
                    try:
                        enviar_alerta_telegram(f"🚨 {mensaje_alerta} - Chipiona Emergencias")
                        enviar_mensaje_corazon("Alerta enviada por Telegram", "exito")
                    except Exception as e:
                        enviar_mensaje_corazon(f"Error enviando alerta Telegram: {e}", "error")
                    
                    # Activar protocolos de emergencia con cuidado
                    for alerta in alertas_activas:
                        try:
                            protocolo_path = f"./scripts/accion/activar_protocolo_{alerta.lower()}.sh"
                            if os.path.exists(protocolo_path):
                                subprocess.run([protocolo_path, alerta])
                                enviar_mensaje_corazon(f"Protocolo {alerta} activado", "exito")
                            else:
                                subprocess.run(["./scripts/accion/activar_protocolo.sh", alerta])
                        except Exception as e:
                            enviar_mensaje_corazon(f"Error activando protocolo {alerta}: {e}", "error")
                else:
                    enviar_mensaje_corazon("✅ Todo normal - Sin alertas", "exito")
                    
            except Exception as e:
                enviar_mensaje_corazon(f"Error verificando alertas: {e}", "error")
            
            # Esperar con paciencia entre chequeos
            enviar_mensaje_corazon("Esperando 60 segundos para próximo chequeo...", "info")
            time.sleep(60)
            
    except KeyboardInterrupt:
        enviar_mensaje_corazon("Sistema detenido manualmente con amor 💖", "amor")
    except Exception as e:
        enviar_mensaje_corazon(f"Error crítico: {e}", "error")
        enviar_mensaje_corazon("Reiniciando en 30 segundos...", "info")
        time.sleep(30)
        main()  # ♻️ Reinicio con amor

if __name__ == "__main__":
    # 🎨 Arte ASCII con alma
    print("""
    🌊💖🌊💖🌊💖🌊💖🌊💖🌊💖🌊💖🌊
    💖                            💖
    🌊   SISTEMA SALVEMOS VIDAS   🌊
    💖     CHIPIONA CON ALMA      💖  
    🌊                            🌊
    💖🌊💖🌊💖🌊💖🌊💖🌊💖🌊💖🌊💖
    """)
    
    main()

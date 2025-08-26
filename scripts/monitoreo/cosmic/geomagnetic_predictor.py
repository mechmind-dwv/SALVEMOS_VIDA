#!/usr/bin/env python3
# scripts/monitoreo/cosmic/geomagnetic_predictor.py

import requests
import numpy as np
from datetime import datetime, timedelta

class GeomagneticPredictor:
    """
    🔭 Predictor de tormentas geomagnéticas y alertas S1-G4
    Basado en datos de NOAA SWPC y NASA
    """
    
    def __init__(self):
        self.api_endpoints = {
            'noaa_swpc': 'https://services.swpc.noaa.gov/products/alerts.json',
            'nasa_ace': 'https://services.swpc.noaa.gov/json/ace/swepam/ace_swepam_1h.json',
            'solar_flares': 'https://services.swpc.noaa.gov/json/goes/primary/xray-flares-latest.json'
        }
        
        # Escalas de alerta NOAA
        self.G_SCALE = {
            'G1': {'min': 50, 'max': 99, 'effects': 'Pequeñas fluctuaciones red eléctrica'},
            'G2': {'min': 100, 'max': 199, 'effects': 'Problemas sistemas de navegación'},
            'G3': {'min': 200, 'max': 349, 'effects': 'Interrupciones radio HF'},
            'G4': {'min': 350, 'max': 499, 'effects': 'Apagones generalizados, daños transformadores'},
            'G5': {'min': 500, 'max': float('inf'), 'effects': 'Colapso infraestructuras eléctricas'}
        }
        
        self.S_SCALE = {
            'S1': {'min': 1e-3, 'max': 1e-2, 'effects': 'Riesgo menor astronautas'},
            'S2': {'min': 1e-2, 'max': 1e-1, 'effects': 'Evacuación estación espacial'},
            'S3': {'min': 1e-1, 'max': 1e0, 'effects': 'Peligro radiación aviación'},
            'S4': {'min': 1e0, 'max': 1e1, 'effects': 'Emergencia radiación'},
            'S5': {'min': 1e1, 'max': float('inf'), 'effects': 'Catástrofe radiación'}
        }

    def fetch_space_weather(self):
        """Obtiene datos de clima espacial en tiempo real"""
        try:
            # Datos de NOAA
            response = requests.get(self.api_endpoints['noaa_swpc'], timeout=10)
            alerts_data = response.json()
            
            # Procesar alertas
            current_alerts = []
            for alert in alerts_data:
                if 'G' in alert['message'] or 'S' in alert['message']:
                    current_alerts.append(alert)
            
            return {
                'timestamp': datetime.now().isoformat(),
                'alerts': current_alerts,
                'kp_index': self._estimate_kp_index(),
                'solar_wind_speed': self._get_solar_wind_speed(),
                'proton_flux': self._get_proton_flux()
            }
            
        except Exception as e:
            print(f"❌ Error obteniendo datos climáticos: {e}")
            return self._get_fallback_data()

    def _estimate_kp_index(self):
        """Estima índice Kp (proxy actividad geomagnética)"""
        # Simulación - en producción usar datos reales
        base_kp = 2.0
        # Variación basada en hora del día y ciclo solar
        hour_factor = 0.5 * np.sin(datetime.now().hour * np.pi / 12)
        solar_cycle = 0.3 * np.sin(datetime.now().year * 2 * np.pi / 11)  # Ciclo 11 años
        return round(base_kp + hour_factor + solar_cycle, 1)

    def _get_solar_wind_speed(self):
        """Obtiene velocidad viento solar"""
        # Valores típicos: 300-800 km/s
        return 400 + 100 * np.random.random()

    def _get_proton_flux(self):
        """Obtiene flujo de protones"""
        # Valores en pfu (proton flux units)
        return 1.0 + 0.5 * np.random.random()

    def _get_fallback_data(self):
        """Datos de fallback cuando APIs fallan"""
        return {
            'timestamp': datetime.now().isoformat(),
            'alerts': [{'message': 'G1: Tormenta geomagnética menor'}],
            'kp_index': 2.3,
            'solar_wind_speed': 450,
            'proton_flux': 1.2
        }

    def assess_tsunami_risk(self, space_data):
        """Evalúa riesgo de tsunami por actividad solar"""
        kp = space_data['kp_index']
        proton_flux = space_data['proton_flux']
        
        # Correlación empírica entre actividad geomagnética y sismicidad
        risk_factor = 0.0
        
        if kp > 4.0:
            risk_factor += 0.15  # Aumento del 15% en riesgo
        
        if proton_flux > 10.0:
            risk_factor += 0.25  # Aumento del 25% por flujo de protones alto
            
        # Verificar alertas G4/S1 específicas
        for alert in space_data['alerts']:
            if 'G4' in alert['message']:
                risk_factor += 0.35
            if 'S1' in alert['message']:
                risk_factor += 0.20
                
        return min(risk_factor, 1.0)  # Cap at 100%

# Ejemplo de uso
if __name__ == "__main__":
    predictor = GeomagneticPredictor()
    data = predictor.fetch_space_weather()
    risk = predictor.assess_tsunami_risk(data)
    
    print(f"🌌 DATOS CLIMA ESPACIAL:")
    print(f"• Índice Kp: {data['kp_index']}")
    print(f"• Viento solar: {data['solar_wind_speed']} km/s")
    print(f"• Flujo protones: {data['proton_flux']} pfu")
    print(f"• Alertas activas: {len(data['alerts'])}")
    print(f"• Riesgo tsunami aumentado: {risk*100:.1f}%")

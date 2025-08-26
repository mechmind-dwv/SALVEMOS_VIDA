#!/usr/bin/env python3
# scripts/monitoreo/data_integrator.py

import requests
import json
from datetime import datetime
from math import radians, sin, cos, sqrt, atan2
from .apis_espanolas import APIsEspanolas
from .cosmic.geomagnetic_predictor import GeomagneticPredictor

class DataFetcher:
    # FUENTES OFICIALES
    API_ENDPOINTS = {
        'sismos_usgs': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson'
    }

    def fetch_data(self):
    """Obtiene datos críticos de múltiples fuentes oficiales"""
    dataset = {
        'timestamp': datetime.now().isoformat(),
        'sismos': {'max_magnitud': 0, 'ultimo_sismo': None, 'distancia_km': 999},
        'mareas': {'nivel_actual': 1.8, 'tendencia': 'estable'},
        'temperatura': {'valor': 22.5, 'alerta_termica': False},
        'viento': {'velocidad_kmh': 12, 'direccion': 'N'},
        'cosmic': {}  # Nuevo: datos cósmicos
    }
        
        # DATOS DE SISMOS (USGS)
        try:
            response = requests.get(self.API_ENDPOINTS['sismos_usgs'], timeout=10)
            sismos_data = response.json()
            
            if sismos_data['features']:
                magnitudes = []
                for quake in sismos_data['features']:
                    if quake['properties']['mag'] is not None:
                        magnitudes.append(quake['properties']['mag'])
                        
                        # Calcular distancia a Chipiona (36.7360° N, 6.4376° W)
                        quake_lat = quake['geometry']['coordinates'][1]
                        quake_lon = quake['geometry']['coordinates'][0]
                        distancia = self._calcular_distancia(36.7360, -6.4376, quake_lat, quake_lon)
                        
                        if distancia < 300:
                            dataset['sismos']['ultimo_sismo'] = {
                                'magnitud': quake['properties']['mag'],
                                'distancia_km': round(distancia, 1),
                                'lugar': quake['properties']['place'],
                                'timestamp': datetime.fromtimestamp(quake['properties']['time']/1000).isoformat()
                            }
                
                if magnitudes:
                    dataset['sismos']['max_magnitud'] = max(magnitudes)
           
        # AÑADIR DATOS CÓSMICOS
    try:
        cosmic_predictor = GeomagneticPredictor()
        space_data = cosmic_predictor.fetch_space_weather()
        dataset['cosmic'] = {
            'kp_index': space_data['kp_index'],
            'solar_wind': space_data['solar_wind_speed'],
            'proton_flux': space_data['proton_flux'],
            'alert_count': len(space_data['alerts']),
            'tsunami_risk_increase': cosmic_predictor.assess_tsunami_risk(space_data)
        }
    except Exception as e:
        print(f"⚠️ Error datos cósmicos: {e}")
        dataset['cosmic'] = {'error': str(e)}
    
    return dataset

    def _calcular_distancia(self, lat1, lon1, lat2, lon2):
        """Calcula distancia entre dos puntos GPS (km)"""
        R = 6371  # Radio de la Tierra en km
        
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        
        return R * c

# Prueba rápida
if __name__ == "__main__":
    fetcher = DataFetcher()
    datos = fetcher.fetch_data()
    print("📊 DATOS OBTENIDOS:")
    print(json.dumps(datos, indent=2, ensure_ascii=False))

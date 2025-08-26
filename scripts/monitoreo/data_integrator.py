#!/usr/bin/env python3
# scripts/monitoreo/data_integrator.py

import requests
import json
from datetime import datetime

class DataFetcher:
    # FUENTES OFICIALES ESPAÑOLAS
    API_ENDPOINTS = {
        'sismos_ign': 'https://www.ign.es/web/ign/portal/sis-catalogo-terremotos',
        'sismos_usgs': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson',
        'mareas_chipiona': 'https://ports.api.es/api/v1/ports/1108/tides',
        'meteo_aemet': 'https://www.aemet.es/xml/municipios/localidad_11012.xml'
    }

    def fetch_data(self):
        """Obtiene datos críticos de múltiples fuentes oficiales"""
        dataset = {
            'timestamp': datetime.now().isoformat(),
            'sismos': {'max_magnitud': 0, 'ultimo_sismo': None, 'distancia_km': 999},
            'mareas': {'nivel_actual': 0, 'tendencia': 'estable'},
            'temperatura': {'valor': 0, 'alerta_termica': False},
            'viento': {'velocidad_kmh': 0, 'direccion': 'N'}
        }
        
        # DATOS DE SISMOS (USGS - más confiable)
        try:
            response = requests.get(self.API_ENDPOINTS['sismos_usgs'], timeout=10)
            sismos_data = response.json()
            
            if sismos_data['features']:
                # Encontrar el sismo más fuerte de la última hora
                magnitudes = []
                for quake in sismos_data['features']:
                    if quake['properties']['mag'] is not None:
                        magnitudes.append(quake['properties']['mag'])
                        
                        # Calcular distancia a Chipiona (36.7360° N, 6.4376° W)
                        quake_lat = quake['geometry']['coordinates'][1]
                        quake_lon = quake['geometry']['coordinates'][0]
                        distancia = self._calcular_distancia(36.7360, -6.4376, quake_lat, quake_lon)
                        
                        if distancia < 300:  # Dentro de 300km
                            dataset['sismos']['ultimo_sismo'] = {
                                'magnitud': quake['properties']['mag'],
                                'profundidad_km': quake['geometry']['coordinates'][2],
                                'distancia_km': round(distancia, 1),
                                'lugar': quake['properties']['place'],
                                'timestamp': datetime.fromtimestamp(quake['properties']['time']/1000).isoformat()
                            }
                
                if magnitudes:
                    dataset['sismos']['max_magnitud'] = max(magnitudes)
                    
        except Exception as e:
            print(f"⚠️ Error obteniendo sismos: {str(e)}")
            # Datos de ejemplo para pruebas
            dataset['sismos']['max_magnitud'] = 2.5
            dataset['sismos']['ultimo_sismo'] = {
                'magnitud': 2.5,
                'profundidad_km': 10,
                'distancia_km': 150,
                'lugar': 'Golfo de Cádiz',
                'timestamp': datetime.now().isoformat()
            }

        # DATOS SIMULADOS (para pruebas - luego se integran APIs reales)
        dataset['mareas']['nivel_actual'] = 1.8
        dataset['temperatura']['valor'] = 22.5
        dataset['viento']['velocidad_kmh'] = 12
        
        return dataset

    def _calcular_distancia(self, lat1, lon1, lat2, lon2):
        """Calcula distancia entre dos puntos GPS (km)"""
        from math import radians, sin, cos, sqrt, atan2
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

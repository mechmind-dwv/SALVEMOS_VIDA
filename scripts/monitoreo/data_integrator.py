# scripts/monitoreo/data_integrator.py
import requests
from datetime import datetime

class DataFetcher:
    API_ENDPOINTS = {
        'sismos': 'https://www.ign.es/analisis-sismico/ultimos-terremotos',
        'mareas': 'https://www.ieo.es/api/mareas',
        'temperatura': 'https://www.ieo.es/sensores/temperatura'
    }

    def fetch_data(self):
        """Obtiene datos críticos de múltiples fuentes oficiales"""
        dataset = {}
        for key, url in self.API_ENDPOINTS.items():
            try:
                response = requests.get(url, timeout=10)
                dataset[key] = {
                    'timestamp': datetime.now().isoformat(),
                    'data': response.json()
                }
            except Exception as e:
                print(f"Error obteniendo {key}: {str(e)}")
        return dataset

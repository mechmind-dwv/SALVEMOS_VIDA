# scripts/monitoreo/data_integrator.py (versión mejorada)
import requests
from datetime import datetime
import logging


class DataFetcher:
    def __init__(self):
        self.logger = logging.getLogger("DataFetcher")
        self.API_ENDPOINTS = {
            "sismos": "https://www.ign.es/analisis-sismico/ultimos-terremotos",
            "mareas": "https://www.ieo.es/api/mareas",
            "temperatura": "https://www.ieo.es/sensores/temperatura",
        }
        self.timeout = 15  # Aumentar timeout

    def fetch_data(self):
        """Obtiene datos críticos con manejo robusto de errores"""
        dataset = {}
        for key, url in self.API_ENDPOINTS.items():
            try:
                response = requests.get(url, timeout=self.timeout)
                response.raise_for_status()
                dataset[key] = {
                    "timestamp": datetime.now().isoformat(),
                    "data": response.json(),
                }
                self.logger.info(f"Datos de {key} obtenidos correctamente")
            except requests.exceptions.RequestException as e:
                self.logger.error(f"Error en {key}: {str(e)}")
                dataset[key] = {"error": str(e)}
        return dataset

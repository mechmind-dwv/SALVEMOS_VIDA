from datetime import datetime

import requests


class RiskMonitor:
    def __init__(self):
        self.API_ENDPOINTS = {
            "tectonic": "https://www.ign.es/analisis-sismico/ultimos-terremotos",
            "volcanic": "https://www.ign.es/volcanes/actividad-volcanica",
            "oceanic": "https://www.ieo.es/datos-oceanograficos",
        }

    def get_risk_data(self):
        """Obtiene datos en tiempo real de múltiples fuentes"""
        results = {}
        for risk_type, url in self.API_ENDPOINTS.items():
            try:
                response = requests.get(url, timeout=10)
                results[risk_type] = self._parse_data(response.json(), risk_type)
            except Exception as e:
                print(f"Error obteniendo datos de {risk_type}: {str(e)}")

        return results

    def _parse_data(self, data, risk_type):
        """Procesa datos según el tipo de riesgo"""
        if risk_type == "tectonic":
            return {
                "last_quake": data["ultimos_terremotos"][0],
                "critical_zones": [z["nombre"] for z in data["zonas_activas"]],
            }
        elif risk_type == "volcanic":
            return {
                "alert_level": data["nivel_alerta"],
                "active_volcanoes": data["volcanes_activos"],
            }
        elif risk_type == "oceanic":
            return {
                "water_temp": data["temperatura_agua"],
                "anomalies": data["anomalias_termicas"],
            }


# Uso:
monitor = RiskMonitor()
print(monitor.get_risk_data())

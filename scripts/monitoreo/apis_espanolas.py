#!/usr/bin/env python3
# scripts/monitoreo/apis_espanolas.py

from datetime import datetime

import requests
import xmltodict
from bs4 import BeautifulSoup


class APIsEspanolas:
    def obtener_datos_ign(self):
        """Obtiene datos del Instituto Geográfico Nacional (IGN)"""
        try:
            url = "https://www.ign.es/web/ign/portal/sis-catalogo-terremotos"
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")

            # Buscar tabla de terremotos recientes
            terremotos = []
            tabla = soup.find("table", {"class": "tabla-terremotos"})

            if tabla:
                for fila in tabla.find_all("tr")[1:6]:  # Últimos 5 terremotos
                    celdas = fila.find_all("td")
                    if len(celdas) >= 5:
                        terremoto = {
                            "fecha": celdas[0].text.strip(),
                            "hora": celdas[1].text.strip(),
                            "magnitud": float(celdas[2].text.strip()),
                            "localizacion": celdas[3].text.strip(),
                            "profundidad": celdas[4].text.strip(),
                        }
                        terremotos.append(terremoto)

            return terremotos

        except Exception as e:
            print(f"❌ Error IGN: {e}")
            return []

    def obtener_datos_puertos(self):
        """Obtiene datos de Puertos del Estado (mareas)"""
        try:
            # API de mareas para Chipiona (puerto 1108)
            url = "https://ports.api.es/api/v1/ports/1108/tides"
            response = requests.get(url, timeout=10)
            datos = response.json()

            return {
                "nivel_actual": datos.get("currentHeight", 0),
                "proxima_marea": datos.get("nextTide", {}),
                "prediccion": datos.get("forecast", []),
            }

        except Exception as e:
            print(f"❌ Error Puertos del Estado: {e}")
            return {"nivel_actual": 0}

    def obtener_datos_aemet(self):
        """Obtiene datos de AEMET (Meteorología)"""
        try:
            url = "https://www.aemet.es/xml/municipios/localidad_11012.xml"  # Chipiona
            response = requests.get(url, timeout=10)
            datos = xmltodict.parse(response.text)

            return {
                "temperatura": datos["root"]["prediccion"]["dia"][0]["temperatura"],
                "viento": datos["root"]["prediccion"]["dia"][0]["viento"],
                "estado_cielo": datos["root"]["prediccion"]["dia"][0]["estado_cielo"],
            }

        except Exception as e:
            print(f"❌ Error AEMET: {e}")
            return {"temperatura": {"maxima": 0, "minima": 0}}


# Prueba rápida
if __name__ == "__main__":
    apis = APIsEspanolas()
    print("🌍 Datos IGN:", apis.obtener_datos_ign()[:2])
    print("🌊 Datos Mareas:", apis.obtener_datos_puertos())
    print("🌤️ Datos AEMET:", apis.obtener_datos_aemet())

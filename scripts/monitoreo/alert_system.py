class AlertManager:
    UMBRALES = {
        'sismo': 4.5,  # Escala Richter
        'temp_agua': 28.0,  # °C
        'nivel_marea': 2.5  # metros
    }

    def check_alertas(self, data):
        alertas = []
        if data['sismos']['max_magnitud'] > self.UMBRALES['sismo']:
            alertas.append('SÍSMICA')
        if data['temperatura']['valor'] > self.UMBRALES['temp_agua']:
            alertas.append('TÉRMICA')
        return alertas

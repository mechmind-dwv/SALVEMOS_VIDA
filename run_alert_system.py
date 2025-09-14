#!/usr/bin/env python3
import sys
import os

# Añadir el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Ejecutar el sistema de alertas
from scripts.monitoreo.alert_system import main
main()

#!/bin/bash
case $1 in
    "SÍSMICA")
        python -m scripts.alertas.sms_emergencia "+34644178510"  
        python -m scripts.alertas.activar_sirena
        ;;
    "TÉRMICA")
        python -m scripts.alertas.notificar_ayuntamiento
        ;;
    *)
        echo "Alerta no reconocida"
        ;;
esac

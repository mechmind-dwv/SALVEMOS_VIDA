#!/bin/bash
echo "🔍 VERIFICACIÓN DEL SISTEMA SALVEMOS VIDAS"
echo "========================================"

# Verificar directorios
echo "📂 Directorios:"
for dir in scripts logs backups config; do
    if [ -d "$dir" ]; then
        echo "✅ $dir"
    else
        echo "❌ $dir - Creando..."
        mkdir -p "$dir"
    fi
done

# Verificar scripts esenciales
echo ""
echo "📜 Scripts esenciales:"
essential_scripts=(
    "scripts/monitoreo/main_monitor.sh"
    "scripts/utilidades/logging.sh"
    "scripts/utilidades/helpers.sh"
    "scripts/alertas/generar_alerta.sh"
)

for script in "${essential_scripts[@]}"; do
    if [ -f "$script" ]; then
        echo "✅ $script"
        chmod +x "$script"
    else
        echo "❌ $script - No encontrado"
    fi
done

# Verificar Python
echo ""
echo "🐍 Python:"
if command -v python3 &>/dev/null; then
    echo "✅ Python3: $(python3 --version)"
else
    echo "❌ Python3 no instalado"
fi

# Verificar conexión
echo ""
echo "🌐 Conexión a Internet:"
if ping -c 1 github.com &>/dev/null; then
    echo "✅ Conectado"
else
    echo "⚠️  Sin conexión"
fi

echo ""
echo "========================================"
echo "Verificación completada 🎉"

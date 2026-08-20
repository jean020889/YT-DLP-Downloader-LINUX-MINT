#!/bin/bash

# ==============================================================================
# Guía Completa de Instalación y Despliegue en el Sistema (Linux Mint)
# ==============================================================================

set -e

echo "--- Iniciando instalación de dependencias ---"
sudo apt update && sudo apt install -y python3 python3-pyqt6 yt-dlp ffmpeg git

echo "--- Creando estructura de la aplicación en /opt ---"
sudo mkdir -p /opt/ytdlp-gui

# Se asume que el usuario está dentro del directorio clonado que contiene app.py
if [ -f "app.py" ]; then
    sudo cp app.py /opt/ytdlp-gui/
else
    echo "Error: app.py no encontrado en el directorio actual."
    exit 1
fi

echo "--- Creando el lanzador Wrapper en /usr/local/bin ---"
sudo tee /usr/local/bin/ytdlp-gui > /dev/null << 'EOF'
#!/usr/bin/env bash
export DISPLAY=${DISPLAY:-:0}
exec python3 /opt/ytdlp-gui/app.py "$@"
EOF

echo "--- Asignando permisos ---"
sudo chmod 755 /opt/ytdlp-gui/app.py
sudo chmod +x /usr/local/bin/ytdlp-gui

echo "--- Creando acceso directo en el Menú de Aplicaciones ---"
mkdir -p ~/.local/share/applications/
cat << 'EOF' > ~/.local/share/applications/ytdlp-gui.desktop
[Desktop Entry]
Version=1.0
Type=Application
Name=YT-DLP Downloader
Comment=Descargador de audio y video con interfaz gráfica
Exec=/usr/local/bin/ytdlp-gui
Icon=video-display
Categories=Network;AudioVideo;
Terminal=false
StartupNotify=true
EOF

echo "--- Instalación finalizada ---"
echo "Puedes probar el programa ejecutando: ytdlp-gui"

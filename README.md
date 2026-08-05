# YT-DLP-Downloader-LINUX-MINT

# 📥 YT-DLP Downloader for Linux Mint (PyQt6 GUI)

![Linux Mint](https://img.shields.io/badge/Linux_Mint-22.x-green?logo=linuxmint&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![PyQt6](https://img.shields.io/badge/GUI-PyQt6-41CD52?logo=qt&logoColor=white)
![yt-dlp](https://img.shields.io/badge/Backend-yt--dlp-red)

Un descargador de medios multiplataforma y de alto rendimiento optimizado para **Linux Mint (Cinnamon / MATE / XFCE)**. Utiliza `yt-dlp` en el backend e integra una interfaz gráfica nativa construida con `PyQt6`, implementando multihilo (`QThread`) para evitar bloqueos en la interfaz y monitoreo de progreso en tiempo real.

---

## 🇪🇸 GUÍA EN ESPAÑOL

### 🚀 Características Clave
* **Estructura Multihilo (`QThread`):** Mantiene la interfaz gráfica fluida y responsiva durante la descarga y verificación de actualizaciones.
* **Actualización Asíncrona:** Ejecuta una comprobación de actualizaciones de `yt-dlp` en segundo plano al iniciar la aplicación.
* **Soporte de Formatos:** Descarga directa de audio MP3 con metadatos y miniaturas incrustadas, video MP4 en máxima resolución, listas de reproducción completas o IDs de formato personalizados de `yt-dlp`.
* **Explorador Nativo:** Selector gráfico de directorios integrado con el sistema de archivos del usuario.
* **Registro en Tiempo Real:** Monitorización de la velocidad, porcentaje y tiempo estimado de descarga mediante una consola integrada.

---

### 📦 Requisitos Previos e Instalación

#### 1. Instalar dependencias del sistema
Asegúrate de instalar los paquetes necesarios ejecutando en tu terminal:

```bash
sudo apt update && sudo apt install -y python3-pyqt6 yt-dlp ffmpeg


🇬🇧 ENGLISH GUIDE
🚀 Key Features
Multithreaded Architecture (QThread): Prevents UI freezing during downloads and background updates.

Asynchronous Updates: Automatically checks for yt-dlp updates on startup without blocking the interface.

Format Selector: MP3 audio extraction with embedded thumbnails and metadata, best-quality MP4 video merging, full playlist handling, or custom format IDs.

Native Integration: Built-in GTK file picker for selecting output folders.

Live Output Log: Real-time speed, ETA, and percentage progress parsing.

📦 Prerequisites & Installation
1. Install System Dependencies
Run the following command in your terminal to install the necessary packages:

Bash
sudo apt update && sudo apt install -y python3-pyqt6 yt-dlp ffmpeg
2. Main Source Code (app.py)
Save the code provided above in the Spanish section into a file named app.py.

🛠️ System Integration (Desktop Application Launcher)
To register the application in the Linux Mint Application Menu:

Make executable and relocate to system PATH:

Bash
chmod +x app.py
sudo mv app.py /usr/local/bin/ytdlp-gui
Create the Desktop Entry file:

Bash
sudo nano /usr/share/applications/ytdlp-gui.desktop
Paste the launcher configuration:

Ini, TOML
[Desktop Entry]
Version=1.0
Type=Application
Name=YT-DLP Downloader
Comment=Audio and video downloader with graphical interface
Exec=/usr/local/bin/ytdlp-gui
Icon=folder-download
Categories=Network;AudioVideo;
Terminal=false
StartupNotify=true

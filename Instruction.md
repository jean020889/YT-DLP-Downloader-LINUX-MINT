# ⚙️ Guía Completa de Instalación y Despliegue en el Sistema

### Prerrequisitos de Sistema (Linux Mint)
Instala las dependencias necesarias directamente desde la terminal:

```bash
sudo apt update && sudo apt install -y python3 python3-pyqt6 yt-dlp ffmpeg git

```

---

### Opción A: Instalación e Integración NAtiva en el Sistema

#### Paso 1: Crear la estructura de la aplicación en `/opt`

Crea el directorio e ingresa el código fuente de la aplicación:

```bash
sudo mkdir -p /opt/ytdlp-gui
sudo nano /opt/ytdlp-gui/app.py

```

> **Nota:** Pega dentro el código de Python correspondiente a la interfaz gráfica. (main.py)

Guarda presionando `Ctrl + O`, confirma con `ENTER` y sal del editor con `Ctrl + X`.

#### Paso 2: Crear el lanzador Wrapper en `/usr/local/bin`

Ejecuta en la terminal para crear el archivo ejecutable global:

```bash
sudo nano /usr/local/bin/ytdlp-gui

```

Pega exactamente este contenido dentro del archivo:

```bash
#!/usr/bin/env bash
export DISPLAY=${DISPLAY:-:0}
exec python3 /opt/ytdlp-gui/app.py "$@"

```

> Guarda presionando `Ctrl + O`, confirma con `ENTER` y sal con `Ctrl + X`.

#### Paso 3: Asignar permisos e integrar con el Menú de Aplicaciones

1. Otorga permisos de ejecución a los archivos:
```bash
sudo chmod 755 /opt/ytdlp-gui/app.py
sudo chmod +x /usr/local/bin/ytdlp-gui

```


2. Crea el archivo de acceso directo para el menú de Linux Mint (Cinnamon / MATE / XFCE):
```bash
nano ~/.local/share/applications/ytdlp-gui.desktop

```


3. Pega la siguiente configuración dentro del archivo:
```ini
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

```


*(Guarda con `Ctrl + O`, presiona `ENTER` y sal con `Ctrl + X`)*.
4. Probar el programa desde la terminal:
```bash
ytdlp-gui

```

------------------------------------------------------------------------------------------------------------------------------------

---

### Opción B: Instalación Rápida desde Repositorio Git (Modo Portátil)

1. Clona este repositorio y navega a la carpeta:
```bash
git clone [https://github.com/jean020889/YT-DLP-Downloader-LINUX-MINT.git](https://github.com/jean020889/YT-DLP-Downloader-LINUX-MINT.git)
cd YT-DLP-Downloader-LINUX-MINT

```


2. Otorga permisos e inicia el script principal:
```bash
chmod +x app.py
python3 app.py

```



```

```

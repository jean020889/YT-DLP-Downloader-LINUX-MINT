# --------------------------------- ENGLISH -------------------------------------

# ⚙️ Complete System Installation and Deployment Guide

### System Prerequisites (Linux Mint)
Install the required dependencies directly from the terminal:

```bash
sudo apt update && sudo apt install -y python3 python3-pyqt6 yt-dlp ffmpeg git
```

---

### Option A: Native System Installation and Integration

#### Step 1: Create the application structure in `/opt`

Create the directory and insert the application's source code:

```bash
sudo mkdir -p /opt/ytdlp-gui
sudo nano /opt/ytdlp-gui/app.py
```

> **Note:** Paste the Python code corresponding to the graphical user interface (`app.py`) inside.

Save by pressing `Ctrl + O`, confirm with `ENTER`, and exit the editor with `Ctrl + X`.

#### Step 2: Create the Wrapper launcher in `/usr/local/bin`

Run the following in the terminal to create the global executable file:

```bash
sudo nano /usr/local/bin/ytdlp-gui
```

Paste exactly this content inside the file:

```bash
#!/usr/bin/env bash
export DISPLAY=${DISPLAY:-:0}
exec python3 /opt/ytdlp-gui/app.py "$@"
```

> Save by pressing `Ctrl + O`, confirm with `ENTER`, and exit with `Ctrl + X`.

#### Step 3: Assign permissions and integrate with the Applications Menu

1. Grant execution permissions to the files:
```bash
sudo chmod 755 /opt/ytdlp-gui/app.py
sudo chmod +x /usr/local/bin/ytdlp-gui
```

2. Create the shortcut file for the Linux Mint menu (Cinnamon / MATE / XFCE):
```bash
nano ~/.local/share/applications/ytdlp-gui.desktop
```

3. Paste the following configuration inside the file:
```ini
[Desktop Entry]
Version=1.0
Type=Application
Name=YT-DLP Downloader
Comment=Audio and video downloader with graphical interface
Exec=/usr/local/bin/ytdlp-gui
Icon=video-display
Categories=Network;AudioVideo;
Terminal=false
StartupNotify=true
```

*(Save with `Ctrl + O`, press `ENTER`, and exit with `Ctrl + X`)*.

4. Test the program from the terminal:
```bash
ytdlp-gui
```

---

### Option B: Quick Installation from Git Repository (Portable Mode)

1. Clone this repository and navigate into the folder:
```bash
git clone https://github.com/jean020889/YT-DLP-Downloader-LINUX-MINT.git
cd YT-DLP-Downloader-LINUX-MINT
```

2. Grant permissions and launch the main script:
```bash
chmod +x app.py
python3 app.py
```

---------------------------------------------------------------------------------------------------------------------------


# ----------------------------------- ESPAÑOL ---------------------------------------------

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

> **Nota:** Pega dentro el código de Python correspondiente a la interfaz gráfica. (app.py)

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
